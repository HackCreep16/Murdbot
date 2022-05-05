import discord
import random
import os
import json
import datetime
from datetime import timedelta
from discord.ext import commands


class qotd(commands.Cog):
    client = commands.Bot(command_prefix="h!")

    def __init__(self, client):
        self.client == client

    @commands.command
    async def randnum(self, ctx):
        value = random.randint(5)
        await ctx.send(value)

        with open('qotd_qafase.json') as f:
            json.load(f)


# end
def setup(client):
    client.add_cog(qotd(client))
