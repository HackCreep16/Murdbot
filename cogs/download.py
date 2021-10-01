import json
import aiofiles
import requests
import aiohttp
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot


class download(commands.Cog):
    prefix = "h!"
    client = commands.Bot(command_prefix=prefix, description="Hello", case_insensitive=False)

    def __init__(self, client):
        self.client == client


def setup(client):
    client.add_cog(download(client))
