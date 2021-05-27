from discord.ext import commands
from discord.utils import get

import discord
import os

my_secret = os.environ['TOKEN']

intents= discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='Chef')
async def owner_find(ctx):
    guild_owner = bot.get_user(int(ctx.guild.owner.id))
    await ctx.send(f'Le chef est : {guild_owner.mention}')

@bot.command(name="Officiers")
async def officers_find(ctx):
    role = get(ctx.guild.roles, name="Officier")
    for m in role.members:
        await ctx.send(f'{m.mention}')

bot.run(my_secret)
