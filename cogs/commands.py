import discord
# from main import client
from discord.ext import commands


class commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def github(self, ctx):
        embedVar = discord.Embed(title="Github",
                                 description="The epic repository link: https://github.com/HackCreep16/Murdbot",
                                 color=0x18191C)
        embedVar.set_thumbnail(
            url="https://github.com/HackCreep16/Murdbot/blob/main/Icon_murd/200x%205%20BR%20CHANGE.png?raw=true")
        await ctx.send(embed=embedVar)

    @commands.command()
    async def about(self, ctx):
        embedVar = discord.Embed(title="About the bot",
                                 description="Murdbot is a multi-functional bot that can do fun stuff, moderation stuff, and yea.",
                                 color=0xfc7f03)
        embedVar.set_thumbnail(
            url="https://github.com/HackCreep16/Murdbot/blob/main/Icon_murd/200x%206%20%20TH%20BR%20CHANGE.png?raw=true")
        embedVar.add_field(name="The creator",
                           value="Hey! It's me, the creator of Murdbot- \*cough* murder \*cough*...anyways..Hello! It's me HackCreep16, the creator of Murdbot :D ")
        embedVar.add_field(name="Hey! You can send suggestions here to make our bot better!",
                           value="Fill me up: https://forms.gle/8cNY6RpshPbFj3YD6", inline=False)
        embedVar.add_field(name="Oh, almost forgot! You can submit your own questions to improve QOTD!",
                           value="Fill me up too: https://forms.gle/ZkdL2nnZ4W1K6gTa6")
        embedVar.add_field(name="Have a problem?", value="https://forms.gle/TedCKcy4WPsNooxv9")
        embedVar.add_field(name="pls don't attacc me",
                           value="pls don't \*insert mario screaming* https://bit.ly/3xZeV1I")
        await ctx.send(embed=embedVar)

    # @commands.command()


# async def suicide(self, ctx):
#     embedVar = discord.Embed(title="I want you to know that you're never alone! We need you!",
#                              description="Please call your local therapist, Death is never the option!",
#                              color=0xff70c3)
#     # embedVar.set_thumbnail(
#     #    url="https://media.discordapp.net/attachments/859288134989381653/861370267007713310/59915-aleksandr-ledogorov-310150-unsplash.png")
#
#     embedVar.add_field(name="Suicide Prevention Hotlines",
#                        value="https://suicidepreventionlifeline.org/ https://www.opencounseling.com/suicide-hotlines",
#                        inline=False)
#     embedVar.add_field(name="Phone Number", value="1-800-273-8255", inline=False)
#     await ctx.send(embed=embedVar)

# TODO ADD DESCRIPTION TO ABOUT

# end
def setup(client):
    client.add_cog(commands(client))
