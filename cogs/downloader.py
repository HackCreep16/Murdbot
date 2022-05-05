import discord
import os.path
import asyncio
import emojis
import googleAPI
import youtube_dl
import googlesearch
from main import client
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from discord.ext import commands


class downloader(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def download(self, ctx, arg):

        global downloaded
        embed = discord.Embed(title="What format do you want?", color=0xff984a)
        embed.add_field(name="CD 💿 = MP3", value="Mp3 download")
        embed.add_field(name="DVD 📀 = MP4", value="Mp4 download")
        message = await ctx.send(embed=embed)

        await message.add_reaction('💿')
        await message.add_reaction('📀')

        def bot_check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['💿', '📀']

        member = ctx.author
        link = arg

        while True:
            try:
                reaction, user = await client.wait_for("reaction_add", check=bot_check)
                if str(reaction.emoji) == '💿':
                    await message.delete()
                    await ctx.send("MP3, got it.")

                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '320',
                        }],
                        'outtmpl': f'./cache/{member}.mp3',
                    }
                    # TODO 1
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])

                        downloaded = await ctx.send(file=discord.File(fR'./{member}.mp3'))  # send audio
                        await ctx.send("Here's your freshly downloaded audio!")
                        if downloaded:
                            os.remove(f'./cache/{member}.mp3')
                            print("Deleted audio.")
                        else:
                            await ctx.send("Uh oh, something broke, please try again later.")

                    # downloaded = await ctx.send(file=discord.File(R'./audio.mp3'))

                if str(reaction.emoji) == '📀':
                    await message.delete()
                    await ctx.send("MP4, feelin' fancy.")

                    ydl_opts = {
                        'format': 'bestaudio[ext=mp4]+bestvideo/mp4',
                        'outtmpl': './video.mp4',
                    }

                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])

                        downloaded = await ctx.send(file=discord.File(R'./video.mp4'))  # send audio
                        await ctx.send(
                            "Here's your freshly downloaded video! (Moving to google drive or some other cloud provider, the discord thing is too limited lol)")
                        if downloaded:
                            os.remove("./video.mp4")
                            print("Deleted video.")
                        else:
                            await ctx.send(
                                "Oh, there's a malfunction. Please try again later :) (If the problem persist,file a bug report at: https://forms.gle/8cNY6RpshPbFj3YD6)")

            finally:
                print('Done.')

    # Google Drive catr

        
    


def setup(client):
    client.add_cog(downloader(client))
