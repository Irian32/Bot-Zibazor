import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

my_secret = os.environ['TOKEN']
client.run(my_secret)