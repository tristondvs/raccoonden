import os, random, nextcord, wavelink, youtube_dl, music, ytdlsource
from dotenv import load_dotenv
from nextcord.ext import commands

client_user = "TrashPandaBot"
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")
youtube_dl.utils.bug_reports_message = lambda: ""

ytdl_format_options = {
    "reconnect": "1",
    "reconnect_streamed": "1",
    "reconnect_delay_max": "5",
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


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # process all the bot commands sent here, since the on_message event gets processed with every single message
    await bot.process_commands(message)


# clears chat messages, removing the last sent message by default, up to x messages
@bot.command(pass_context=True)
async def clear(ctx, amount=2):
    if amount >= 2:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.channel.purge(limit=amount)

#confirm if the bot is online
@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send('```online```')

@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Okay, I'm headed out. See you next time!")
    else:
        await ctx.send(
            "```You command echoes throughout the room with no response. Your fuzzy friend is not in a voice channel.```"
        )

bot.add_cog(music.music(bot))
bot.run(TOKEN)
