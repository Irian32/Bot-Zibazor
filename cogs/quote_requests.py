from discord.ext import commands
import random

class quote_requests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Quote')
    async def quote_finder(self, ctx):
        # Get all quote
        f = open("data/quotes.txt", "r")
        quotes = f.read().split("\n\n")
        f.close()

        # Find one random quotes
        quote = random.choice(quotes)

        # Send the quote
        await ctx.send(f'{quote}')



            