import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot


class helppo(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        return await super().send_bot_help(mapping)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super(helppo, self).send_group_help(group)

    async def send_command_help(self, command):
        return await super().send_command_help(command)


class help(commands.Cog):

    prefix = "h!"
    client = commands.Bot(command_prefix=prefix, description="Hello", case_insensitive=False, help_command=helppo())

    def __init__(self, client):
        self.client == client


def setup(client):
    client.add_cog(help(client))
