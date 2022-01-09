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
    await ctx.send(n)

if __name__ == "__main__":
    bot.run()
