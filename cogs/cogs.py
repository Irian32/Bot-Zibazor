from discord.ext import commands
from discord.utils import get

class info_requests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Chef')
    async def owner_find(self, ctx):
        guild_owner = self.bot.get_user(int(ctx.guild.owner.id))
        await ctx.send(f'Le chef est : {guild_owner.mention}')

    @commands.command(name="Officiers")
    async def officers_find(self, ctx):
        officers = get(ctx.guild.roles, name="Officier")
        for officer in officers.members:
            await ctx.send(f'{officer.mention}')

