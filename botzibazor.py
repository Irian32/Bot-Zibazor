import logging
import discord
from discord.ext import commands

from cogs.info_requests import info_requests
from cogs.quote_requests import quote_requests
from cogs.kill_marry_fuck import kill_marry_fuck

class Botzibazor:

    def __init__(self, token):
        self._token = token
        self.intents= discord.Intents.default()
        self.intents.members = True
        self.command_manager = commands.Bot(command_prefix='!', intents=self.intents) 

        # Load cogs (command interpreter and bot listener)
        self.command_manager.add_cog(info_requests(self.command_manager))
        self.command_manager.add_cog(quote_requests(self.command_manager))
        self.command_manager.add_cog(kill_marry_fuck(self.command_manager))

        # On connect event 
        @self.command_manager.event
        async def on_ready():
            logging.info(f'{self.command_manager.user.name} has connected to Discord')

    def start(self):
        self.command_manager.run(self._token)

