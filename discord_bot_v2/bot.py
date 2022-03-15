import os
import random
import nextcord
import youtube_dl
import wavelink
from dotenv import load_dotenv
from nextcord.ext import commands

client_user = "TrashPandaBot"
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")
youtube_dl.utils.bug_reports_message = lambda: ""


ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(nextcord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream)
        )

        if "entries" in data:
            # take first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(nextcord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel=nextcord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
            await channel.connect()
            await ctx.send("I'm ready to jam with you! use $play and give me a URL!")
        else:
            await ctx.send(
                "```Your fuzzy friend's ears perk up to your request; he looks around but can't make out where the voice came from. He seems to not know which room you're in...```"
            )

    # Play a local file
    @commands.command()
    async def play_sound(self, ctx, *, query):
        source = nextcord.PCMVolumeTransformer(nextcord.FFmpegPCMAudio(query))
        ctx.voice_client.play(
            source, after=lambda e: print(f"Player error: {e}") if e else None
        )
        await ctx.send(f"Now playing: {query}")

    @commands.command()
    async def play(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(
                player, after=lambda e: print(f"Player error: {e}") if e else None
            )
        await ctx.send(f"Now playing: {player.title}")

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("I'm not currently in a voice channel.")
        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Okay, I'll change the volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Okay, see you later!")

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send(
                    "```Your command echoes throughout the room with no response. Your fuzzy friend is not in a voice channel with you.```"
                )
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


@bot.event
async def on_ready():
    print(f"{client_user} has connected to Discord!")
    # bot.loop.create_task(node_connect())


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hello there {member.name}, welcome to Tha Dumpsta!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    greetings = [
        '```From the corner of the dumpster, you hear a faint sound of paper crumpling, followed by the tumbling of soda cans. Two glowing green eyes peer at you from across the garbage...``` Hello there! I\'m not quite sure what this means *exactly*, but I was told to let you know, that... ```The stony, jade colored eyes quickly glance at a greasy, crumpled piece of paper stuck to his bottom paw...``` ...That "the docker container is now running"...? Better go catch it!!',
        "```Your voice rings within the steel abode, and echoes into nothingness. You sense that your friend might be sleeping for the time being.```",
        "```Feeling a fuzzy object quickly brush against your right elbow, you quickly turn around in shock and are greeted with a friendly face...``` I didn't mean to sneak up on you there, I was over here organizing my bottlecap collection.",
        "```A dark figure from the other side of the dumpster turns to greet you. Your fuzzy friend raises one hand in greeting, while the other holds a half-eaten slice of pizza. He continues to chew with his mouth closed; we still practice table manners here. Nevertheless, you feel welcome and acknowledged.```",
    ]

    if message.content == "testing":
        response = random.choice(greetings)
        await message.channel.send(response)

    # process all the bot commands sent here, since the on_message event gets processed with every single message
    await bot.process_commands(message)


# clears chat messages, removing the last sent message by default, up to x messages
@bot.command(pass_context=True)
async def clear(ctx, amount=2):
    if amount >= 2:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.channel.purge(limit=amount)


# @bot.command(pass_context=True)
# async def join(ctx):
#    # If a user is within a voice channel:
#    if (ctx.author.voice):
#        channel = ctx.message.author.voice.channel
#        await channel.connect()
#    else:
#        await ctx.send(
#        "```Your fuzzy friend's ears perk up to your request; he looks around but can't make out where the voice came from. He seems to not know which room you're in...```"
#        )


@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Okay, I'm headed out. See you next time!")
    else:
        await ctx.send(
            "```You command echoes throughout the room with no response. Your fuzzy friend is not in a voice channel.```"
        )


bot.add_cog(Music(bot))
bot.run(TOKEN)
