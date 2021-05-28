from discord.ext import commands
import random

class kill_marry_fuck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kmf')
    async def kmf_request(self, ctx):

        f = open("data/kmf.txt", "r")
        names = f.read().split("\n")
        f.close()

        await ctx.send('Kill / Marry / Fuck entre :')
        user1 = random.choice(names)
        names.remove(user1)
        user2 = random.choice(names)
        names.remove(user2)
        user3 = random.choice(names)
        names.remove(user3)

        await ctx.send(f"{user1}, {user2}, {user3}")

    @commands.command(name="rand")
    async def rand_request(self, ctx):
        f = open("data/kmf.txt", "r")
        names = f.read().split("\n")
        f.close()
        await ctx.send(f"{random.choice(names)}")

    