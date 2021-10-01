import json
import aiofiles
import os
import requests
import aiohttp
import discord
from discord.ext import commands
import googleapiclient.discovery
import googleapiclient.errors
from discord.ext.commands import Bot


class music_thing(commands.Cog):
    prefix = "h!"
    client = commands.Bot(command_prefix=prefix, description="Hello", case_insensitive=False)

    def __init__(self, client):
        self.client == client

    # join/leave
    @client.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @client.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(client):
    client.add_cog(music_thing(client))
