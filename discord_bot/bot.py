import os
import discord
import random
from dotenv import load_dotenv

client_user = 'TrashPandaBot'
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client_user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hello there {member.name}, welcome to Tha Dumpsta!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    greetings = [
    '```From the corner of the dumpster, you hear a faint sound of paper crumpling, followed by the tumbling of soda cans. Two glowing green eyes peer at you from across the garbage...``` Hello there! I\'m not quite sure what this means *exactly*, but I was told to let you know, that... ```The stony, jade colored eyes quickly glance at a greasy, crumpled piece of paper stuck to his bottom paw...``` ...That \"the docker container is now running\"...? Better go catch it!!', 
    '```Your voice rings within the steel abode, and echoes into nothingness. You sense that your friend might be sleeping for the time being.```', 
    '```Feeling a fuzzy object quickly brush against your right elbow, you quickly turn around in shock and are greeted with a friendly face...``` I didn\'t mean to sneak up on you there, I was over here organizing my bottlecap collection.'
    ]

    if message.content == 'testing':
        response = random.choice(greetings)
        await message.channel.send(response)

client.run(TOKEN)
