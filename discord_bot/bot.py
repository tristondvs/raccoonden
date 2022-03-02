import os
import discord
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

client.run(TOKEN)
