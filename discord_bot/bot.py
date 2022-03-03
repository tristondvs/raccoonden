import os
from discord.ext import commands
import discord
import random
from dotenv import load_dotenv

client_user = 'TrashPandaBot'
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print(f'{client_user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hello there {member.name}, welcome to Tha Dumpsta!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    greetings = [
    '```From the corner of the dumpster, you hear a faint sound of paper crumpling, followed by the tumbling of soda cans. Two glowing green eyes peer at you from across the garbage...``` Hello there! I\'m not quite sure what this means *exactly*, but I was told to let you know, that... ```The stony, jade colored eyes quickly glance at a greasy, crumpled piece of paper stuck to his bottom paw...``` ...That \"the docker container is now running\"...? Better go catch it!!', 
    '```Your voice rings within the steel abode, and echoes into nothingness. You sense that your friend might be sleeping for the time being.```', 
    '```Feeling a fuzzy object quickly brush against your right elbow, you quickly turn around in shock and are greeted with a friendly face...``` I didn\'t mean to sneak up on you there, I was over here organizing my bottlecap collection.', 
    '```A dark figure from the other side of the dumpster turns to greet you. Your fuzzy friend raises one hand in greeting, while the other holds a half-eaten slice of pizza. He continues to chew with his mouth closed; we still practice table manners here. Nevertheless, you feel welcome and acknowledged.```'
    ]

    if message.content == 'testing':
        response = random.choice(greetings)
        await message.channel.send(response)

    # process all the bot commands sent here, since the on_message event gets processed with every single message
    await bot.process_commands(message)

# clears chat messages, removing the last sent message by default, up to x messages
@bot.command()
async def clear(ctx, amount = 2):
    if amount >= 2:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.channel.purge(limit=amount)

@bot.command(name='join', help='This command will pull TrashPandaBot into your voice chat channel.')
async def join(ctx):
    # If a user is within a voice channel:
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send(
        "```Your fuzzy friend's ears perk up to your request; he looks around but can't make out where the voice came from. He seems to not know which room you're in...```"
        )
        
@bot.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Okay, I'm headed out. See you next time!")
    else:
        await ctx.send("```You command echoes throughout the room with no response. Your fuzzy friend is not in a voice channel.```")

bot.run(TOKEN)
