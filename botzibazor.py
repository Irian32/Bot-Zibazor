import discord
from discord.ext import commands
from cogs import info_requests

class Botzibazor:

    def __init__(self, token):
        self._token = token
        self.intents= discord.Intents.default()
        self.intents.members = True
        self.command_manager = commands.Bot(command_prefix='!', intents=self.intents) 

        # Loads cogs (command interpreter and bot listener)
        self.command_manager.add_cog(info_requests(self.command_manager))

        # On connect event 
        @self.command_manager.event
        async def on_ready():
            print(f'{self.command_manager.user.name} has connected to Discord')


    def start(self):
        self.command_manager.run(self._token)

