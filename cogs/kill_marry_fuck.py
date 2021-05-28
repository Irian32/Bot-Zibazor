from discord.ext import commands
import random

class kill_marry_fuck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kmf')
    async def kmf_request(self, ctx):

        await ctx.send('Kill / Marry / Fuck entre :')
        users = ctx.guild.members
        user1 = random.choice(users)
        users.remove(user1)
        user2 = random.choice(users)
        users.remove(user2)
        user3 = random.choice(users)
        users.remove(user3)

        await ctx.send(f"{user1.name}, {user2.name}, {user3.name}")

    @commands.command(name="rand")
    async def rand_request(self, ctx):
        await ctx.send(f"{random.choice(ctx.guild.members).name}")