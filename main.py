import json
import discord
import os
from discord.ext import commands

prefix = "h!"
client = commands.Bot(command_prefix=prefix, description="Hello", case_insensitive=False)
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name="Death", url="https://www.youtube.com/watch?v=1G-tJsFfo2I"))
    print('I logged on as a hunter')  # idk


# Commands

@client.command()
async def explode(ctx, * message):
    await ctx.send("don't make him do that 3:|")
    await message.delete()


# TODO Organfailureisnotwhatimgonnabehaving

# cog initiator

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# run bot
client.run('insert token')
