import os
from dotenv import load_dotenv
from fbchat import Client
from fbchat.models import Message

load_dotenv()
# sourced in .env file
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

# logging in
client = Client(username, password)

users = client.fetchThreadList()
print(users)
