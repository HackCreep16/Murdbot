import os
import discord
from discord.ext import commands


# something
class helppo(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send(f'')

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super(helppo, self).send_group_help(group)

    async def send_command_help(self, command):
        return await super().send_command_help(command)


prefix = "h!"
client = commands.Bot(command_prefix=prefix, description="Hello", case_insensitive=False, help_command=helppo())


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name="Death", url="https://www.youtube.com/watch?v=1G-tJsFfo2I"))
    print('I logged on as a hunter')  # idk

@client.command()
async def Explode(ctx):
    await ctx.send("don't make him do that 3:|")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# e | Run
client.run('[Insert token here]')
