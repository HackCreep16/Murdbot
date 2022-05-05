import json
import aiofiles
import requests
import aiohttp
import discord
from time import sleep
from random import randint
from main import client
from discord.ext import commands


class fun_stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    # random dog image
    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()

            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()

        embed = discord.Embed(title="A doggo for you", color=0x91572a)
        embed.set_image(url=dogjson['link'])
        embed.add_field(name='Fun Fact: ', value= factjson['fact'], inline=False)
        await ctx.send(embed=embed)

    # random cat image
    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://thecatapi.com/v1/images?api_key=9427129d-8062-4c87-8603-f1e044de68e9')
            catjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()

        embed = discord.Embed(title="A catto for you", color=0xff984a)
        embed.set_image(url=catjson['link'])
        embed.add_field(name="about", value="Shows the epic about page about this bot.", inline=False)
        await ctx.send(embed=embed)

    # random panda image
    @commands.command()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            pandajson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/panda')
            factjson = await request2.json()

        embed = discord.Embed(title="A catto for you", color=0xff984a)
        embed.set_image(url=pandajson['link'])
        embed.add_field(name="about", value="Shows the epic about page about this bot.", inline=False)
        await ctx.send(embed=embed)

    # random fox image
    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            foxjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/fox')
            factjson = await request2.json()

        embed = discord.Embed(title="A catto for you", color=0xff984a)
        embed.set_image(url=foxjson['link'])
        embed.add_field(name="about", value="Shows the epic about page about this bot.", inline=False)
        await ctx.send(embed=embed)

    # random red panda image
    @commands.command()
    async def redpanda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/red_panda')
            redpandajson = await request.json()
            request2 = await session.get('https://some-random-api.ml/animal/red_panda')
            redpandajson = await request.json(redpandajson)
        embed = discord.Embed(title="A red pandaw for you", color=0xff984a)
        embed.set_image(url=redpandajson['link'])
        await ctx.send(embed=embed)

    # random koala image
    @commands.command()
    async def koala(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/koala')
            koalajson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/red_panda')
            factjson = await request2.json()

        embed = discord.Embed(title="A catto for you", color=0xff984a)
        embed.set_image(url=koalajson['link'])
        embed.add_field(name="about", value="Shows the epic about page about this bot.", inline=False)
        await ctx.send(embed=embed)

    # random bird image
    @commands.command()
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/bird')
            birdjson = await request.json()
        embed = discord.Embed(title="A catto for you", color=0xff984a)
        embed.set_image(url=birdjson['link'])
        await ctx.send(embed=embed)

    # random raccoon image
    @commands.command()
    async def raccoon(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/raccoon')
            raccoonjson = await request.json()
        embed = discord.Embed(title="A cute racoon for you.", color=0xff984a)

        embed.set_footer(text='Agent R wants to know your location')

        embed.set_image(url=raccoonjson['link'])
        await ctx.send(embed=embed)

    # random kangaroo image
    @commands.command()
    async def kangaroo(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/kangaroo')
            kangaroojson = await request.json()
        embed = discord.Embed(title="A cool kangaroo for you", color=0xff984a)
        embed.set_image(url=kangaroojson['link'])
        await ctx.send(embed=embed)


    @commands.command()
    async def fact(self, ctx):
        embed = discord.Embed(title="Fun fact")


# end
def setup(client):
    client.add_cog(fun_stuff(client))
