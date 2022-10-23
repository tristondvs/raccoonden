# sauce :
# bot: https://gist.github.com/aliencaocao/83690711ef4b6cec600f9a0d81f710e5
# YouTube_DL: https://github.com/yt-dlp/yt-dlp#installation
# ffmpeg static builds: https://github.com/yt-dlp/FFmpeg-Builds

import os, sys
import re
import time
import atexit
from typing import Dict, List
import logging
import asyncio
import requests
import urllib.parse, urllib.request
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import yt_dlp

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

sys.path.append('.')
logging.basicConfig(level=logging.WARNING)
yt_dlp.utils.bug_reports_message = lambda: ''  # disable yt_dlp bug report
intents = nextcord.Intents.default()
# noinspection PyDunderSlots
intents.message_content = True
help_command = commands.DefaultHelpCommand(no_category='Commands')  # Change only the no_category default string
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), intents=intents, help_command=help_command, strip_after_prefix=True, description='TrashPandaBot Help')

ytdl_format_options = {'format': 'bestaudio',
                       'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                       'restrictfilenames': True,
                       'no-playlist': True,
                       'nocheckcertificate': True,
                       'ignoreerrors': False,
                       'logtostderr': False,
                       'geo-bypass': True,
                       'quiet': True,
                       'no_warnings': True,
                       'default_search': 'auto',
                       'source_address': '0.0.0.0'}
ffmpeg_options = {'options': '-vn -sn'}
ytdl = yt_dlp.YoutubeDL(ytdl_format_options)


class Source:
    """Parent class of all music sources"""

    def __init__(self, audio_source: nextcord.AudioSource, metadata):
        self.audio_source: nextcord.AudioSource = audio_source
        self.metadata = metadata
        self.title: str = metadata.get('title', 'Unknown title')
        self.url: str = metadata.get('url', 'Unknown URL')

    def __str__(self):
        return f'{self.title} ({self.url})'


class YTDLSource(Source):
    """Subclass of YouTube sources"""

    def __init__(self, audio_source: nextcord.AudioSource, metadata):
        super().__init__(audio_source, metadata)
        self.url: str = metadata.get('webpage_url', 'Unknown URL')  # yt-dlp specific key name for original URL

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        metadata = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in metadata: metadata = metadata['entries'][0]
        filename = metadata['url'] if stream else ytdl.prepare_filename(metadata)
        return cls(await nextcord.FFmpegOpusAudio.from_probe(filename, **ffmpeg_options), metadata)


class ServerSession:
    def __init__(self, guild_id, voice_client):
        self.guild_id: int = guild_id
        self.voice_client: nextcord.VoiceClient = voice_client
        self.queue: List[Source] = []

    def display_queue(self) -> str:
        currently_playing = f'Currently playing: 0. {self.queue[0]}'
        return currently_playing + '\n' + '\n'.join([f'{i + 1}. {s}' for i, s in enumerate(self.queue[1:])])

    async def add_to_queue(self, ctx, url):  # does not auto start playing the playlist
        yt_source = await YTDLSource.from_url(url, loop=bot.loop, stream=False)  # stream=True has issues and cannot use Opus probing
        self.queue.append(yt_source)
        if self.voice_client.is_playing():
            async with ctx.typing():
                await ctx.send(f'```Added to queue: {yt_source.title}```')
            pass  # to stop the typing indicator

    async def start_playing(self, ctx):
        async with ctx.typing():
            self.voice_client.play(self.queue[0].audio_source, after=lambda e=None: self.after_playing(ctx, e))
        await ctx.send(f'```Now playing: {self.queue[0].title}```')

    async def after_playing(self, ctx, error):
        if error:
            raise error
        else:
            if self.queue:
                await self.play_next(ctx)

    async def play_next(self, ctx):  # should be called only after making the first element of the queue the song to play
        self.queue.pop(0)
        if self.queue:
            async with ctx.typing():
                await self.voice_client.play(self.queue[0].audio_source, after=lambda e=None: self.after_playing(ctx, e))
            await ctx.send(f'```Now playing: {self.queue[0].title}```')


server_sessions: Dict[int, ServerSession] = {}  # {guild_id: ServerSession}


def clean_cache_files():
    if not server_sessions:  # only clean if no servers are connected
        for file in os.listdir():
            if os.path.splitext(file)[1] in ['.webm', '.mp4', '.m4a', '.mp3', '.ogg'] and time.time() - os.path.getmtime(file) > 7200:  # remove all cached webm files older than 2 hours
                os.remove(file)


def get_res_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller
     Relative path will always get extracted into root!"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    if os.path.isfile(os.path.join(base_path, relative_path)):
        return os.path.join(base_path, relative_path)
    else:
        raise FileNotFoundError(f'```Embedded file {os.path.join(base_path, relative_path)} is not found!```')


@atexit.register
def cleanup():
    global server_sessions
    for vc in server_sessions.values():
        vc.disconnect()
        vc.cleanup()
    server_sessions = {}
    clean_cache_files()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'```{ctx.author}\'s message "{ctx.message.content}" triggered error:\n{error}```')


@bot.command()
@commands.is_owner()
async def debug(ctx, *, code):
    """Only the bot owner can run this, executes arbitrary code"""
    await ctx.send(eval(code))



async def connect_to_voice_channel(ctx, channel):
    voice_client = await channel.connect()
    if voice_client.is_connected():
        server_sessions[ctx.guild.id] = ServerSession(ctx.guild.id, voice_client)
        await ctx.send(f'```Connected to {voice_client.channel.name}```')
        return server_sessions[ctx.guild.id]
    else:
        await ctx.send(f'```Failed to connect to voice channel {ctx.author.voice.channel.name}```')


@bot.command(name='exit')
async def disconnect(ctx):
    """Disconnect from voice channel"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        voice_client = server_sessions[guild_id].voice_client
        await voice_client.disconnect()
        voice_client.cleanup()
        del server_sessions[guild_id]
        await ctx.send(f'```Disconnected from {voice_client.channel.name}```')


@bot.command()
async def pause(ctx):
    """Pause the current song"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        voice_client = server_sessions[guild_id].voice_client
        if voice_client.is_playing():
            voice_client.pause()
            await ctx.send('```Paused```')


@bot.command()
async def resume(ctx):
    """Resume the current song"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        voice_client = server_sessions[guild_id].voice_client
        if voice_client.is_paused():
            voice_client.resume()
            await ctx.send('```Resumed```')


@bot.command()
async def skip(ctx):
    """Skip the current song"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        session = server_sessions[guild_id]
        voice_client = session.voice_client
        if voice_client.is_playing():
            if len(session.queue) > 1:
                voice_client.stop()  # this will trigger after_playing callback and in that will call play_next so here no need call play_next
            else:
                await ctx.send('```This is already the last song in the queue```')


@bot.command(name='queue')
async def show_queue(ctx):
    """Show the current queue"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        await ctx.send(f'{server_sessions[guild_id].display_queue()}')


@bot.command()
async def remove(ctx, i: int):
    """Remove an item from queue by index (1, 2...)"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        if i == 0:
            await ctx.send('```Cannot remove current playing song, please use !skip instead```')
        elif i >= len(server_sessions[guild_id].queue):
            await ctx.send(f'```The queue is not that long, there are only {len(server_sessions[guild_id].queue)-1} items in the queue```')
        else:
            removed = server_sessions[guild_id].queue.pop(i)
            removed.audio_source.cleanup()
            await ctx.send(f'```Removed {removed} from queue```')


@bot.command()
async def clear(ctx):
    """Clear the entire queue and stop the current playing song"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        voice_client = server_sessions[guild_id].voice_client
        server_sessions[guild_id].queue = []
        if voice_client.is_playing():
            voice_client.stop()
        await ctx.send('```Queue cleared```')


@bot.command()
async def song(ctx):
    """Show the current song"""
    guild_id = ctx.guild.id
    if guild_id in server_sessions:
        await ctx.send(f'```Now playing {server_sessions[guild_id].queue[0]}```')


@bot.command()
async def play(ctx, *, query: str):
    """Play a YouTube video by URL if given a URL, or search up the song and play the first video in search result"""
    async with ctx.typing():
        guild_id = ctx.guild.id
        if guild_id not in server_sessions:  # not connected to any VC
            if ctx.author.voice is None:
                await ctx.send(f'```You are not connected to a voice channel```')
                return
            else:
                session = await connect_to_voice_channel(ctx, ctx.author.voice.channel)
        else:  # is connected to a VC
            session = server_sessions[guild_id]
            #if session.voice_client.channel != ctx.author.voice.channel:  # connected to a different VC than the command issuer (but within the same server)
            #    await session.voice_client.move_to(ctx.author.voice.channel)
            #    await ctx.send(f'```Connected to {ctx.author.voice.channel}.')
        try:
            requests.get(query)
        except (requests.ConnectionError, requests.exceptions.MissingSchema):  # if not a valid URL, do search and play the first video in search result
            query_string = urllib.parse.urlencode({"search_query": query})
            formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
            url = f'https://www.youtube.com/watch?v={search_results[0]}'
        else:  # is a valid URL, play directly
            url = query
    await session.add_to_queue(ctx, url)  # will download file here
    if not session.voice_client.is_playing() and len(session.queue) <= 1:
        await session.start_playing(ctx)


clean_cache_files()
bot.run(token)
