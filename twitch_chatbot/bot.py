import os
import random
import asyncio
import mysql.connector
from twitchio.ext import commands

#connect to mysql database
db = mysql.connector.connect(
    host - "localhost",
    user = "root",
    passwd = ""
)

print(db)
cursor = db.cursor()
twitch_user = ctx.author.name
query_play = "UPDATE twitch_info.rps_scores (twitch_user, games_played) VALUES (%s, %s) ON DUPLICATE KEY UPDATE twitch_user = 'str(twitch_user)'"
query_win = "INSERT INTO rps_scores (twitch_user, games_won) VALUES (%s, %s)"
query_lose = "INSERT INTO rps_scores (twitch_user, games_lost) VALUES (%s, %s)"
query_tie = "INSERT INTO rps_scores (twitch_user, games_tied) VALUES (%s, %s)"
# set up the bot
bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

#@bot.command(name='shoutc')
#async def test(ctx, arg=''):
#    clips_list = twitchio.Clip()
#    await ctx.send(f'Sure thing {ctx.author.name}, check out these clips from @{arg}')

@bot.command(name='test')
async def test(ctx):
    await ctx.send('I\'m here Jeezy mormon2L')

@bot.command(name='rand')
async def test(ctx):
    n = random.randint(1,6)
    await ctx.send("/me rolls a fuzzy die, and it landed on a " + str(n))

@bot.command(name='rps')
async def test(ctx, arg='none'):
    n = random.randint(1,3)
    r = 1
    p = 2
    s = 3
    if (arg == "none"):
        await ctx.send(f'@{ctx.author.name},  be sure to call the !rps command while also making your choice. (example: "!rps paper")')
    if (arg == "rock"):
        if (n == 1):
            values = (str(twitch_user), games_played)
            await ctx.send(f'@{ctx.author.name}, I also chose rock, so we tied. mormon2RNG')
        elif (n == 2):
            await ctx.send(f'@{ctx.author.name}, I chose paper, so I win! mormon2LUL')
        else:
            await ctx.send(f'@{ctx.author.name}, I chose scissors, so you win! mormon2HYPE')
    if (arg == "paper"):
        if (n == 1):
            await ctx.send(f'@{ctx.author.name}, I chose rock, so you win! mormon2HYPE')
        if (n == 2):
            await ctx.send(f'@{ctx.author.name}, I also chose paper, so we tied. mormon2RNG')
        if (n == 3):
            await ctx.send(f'@{ctx.author.name}, I chose scissors, so I win! mormon2LUL')
    if (arg == "scissors"):
        if (n == 1):
            await ctx.send(f'@{ctx.author.name}, I chose rock, so I win! mormon2LUL')
        if (n == 2):
            await ctx.send(f'@{ctx.author.name}, I chose paper, so you win! mormon2HYPE')
        if (n == 3):
            await ctx.send(f'@{ctx.author.name}, I also chose scissors, so we tied. mormon2RNG')
    #else:
    #    await ctx.send("You must choose rock, paper, or scissors. Play fair! you can't bring " + arg + " to this battle!")


if __name__ == "__main__":
    bot.run()
