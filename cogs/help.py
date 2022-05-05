import discord
from discord.ext import commands


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(invoke_without_command=True)
    async def help(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(title="help", description="", color=0x4d97ff)

        embed.add_field(name="help", value="Shows the help command to help you.", inline=False)
        embed.add_field(name="about", value="Shows the epic about page about this bot.", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(help(client))
