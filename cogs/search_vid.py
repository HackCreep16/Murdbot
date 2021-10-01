import json
import aiofiles
import requests
import aiohttp
import os
import discord
from discord.ext import commands


class search_vid(commands.Cog):
    prefix = "h!"
    client = commands.Bot(command_prefix=prefix, description="Hello", case_insensitive=False)

    def __init__(self, client):
        self.client == client

def setup(client):
    client.add_cog(search_vid(client))