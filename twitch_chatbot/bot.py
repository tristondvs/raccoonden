import os
import random
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='rand')
async def test(ctx):
    n = random.randint(1,6)
    await ctx.send(str(n))

@bot.command(name='rps')
async def test(ctx, arg='none'):
    n = random.randint(1,3)
    r = 1
    p = 2
    s = 3
    if (arg == "none"):
        await ctx.send('Call the rps command while also making your choice. (example: "!rps paper")')
    if (arg == "rock"):
        if (n == 1):
            await ctx.send('I also chose rock, so we tied. mormon2RNG')
        elif (n == 2):
            await ctx.send('I chose paper, so I win! mormon2LUL')
        else:
            await ctx.send('I chose scissors, so you win! mormon2HYPE')
    if (arg == "paper"):
        if (n == 1):
            await ctx.send('I chose rock, so you win! mormon2HYPE')
        if (n == 2):
            await ctx.send('I also chose paper, so we tied. mormon2RNG')
        if (n == 3):
            await ctx.send('I chose scissors, so I win! mormon2LUL')
    if (arg == "scissors"):
        if (n == 1):
            await ctx.send('I chose rock, so I win! mormon2LUL')
        if (n == 2):
            await ctx.send('I chose paper, so you win! mormon2HYPE')
        if (n == 3):
            await ctx.send('I also chose scissors, so we tied. mormon2RNG')
    #else:
    #    await ctx.send("You must choose rock, paper, or scissors. Play fair! you can't bring " + arg + " to this battle!")


if __name__ == "__main__":
    bot.run()
