import discord
import asyncio
from discord.ext import commands
import youtube_dl
from http import HTTPStatus
import random
from itertools import cycle
import time


client = discord.Client()
token = "ODE1NzA2ODY0NTc0NTI5NTk2.YDwUNw.K6oH2cIWHiRq9nkp87nFIRLwVPo"

@client.event
async def on_ready():
    print(client.user.name)
    print("Loading..")
    print("Success!")
    game = discord.Game("~help")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("~join"):
        await message.author.voice.channel.connect()
    
    if message.content.startswith("~leave"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        
        await voice.disconnect()

    if message.content.startswith("~p"):
        await message.author.voice.channel.connect()
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        url = message.content.split(" ")[1]
        option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio',
                  'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'
        }

        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            info_dict = ydl.extract_info(url, download=False)
            title = info["title"]
            thumbnail = info["thumbnail"]
        
        voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg/bin/ffmpeg.exe', source="file/" + url.split('=')[1] + '.mp3'))
        embed=discord.Embed(title=title, color = 0xff0000, url= url)
        embed.set_image(url=thumbnail)
        await message.channel.send(embed=embed)

    if message.content.startswith("~stop"):
            voice = discord.utils.get(client.voice_clients, guild = message.guild) 
            if voice.is_playing(): 
    	        voice.pause() 
            else:
    	        await message.channel.send("Already stopped")
    
    if message.content.startswith("~resum"):
            voice = discord.utils.get(client.voice_clients, guild = message.guild) 
            if voice.is_paused(): 
    	        voice.resume()
            else:
    	        await message.channel.send("Already started")

    if message.content == "~help":
        embed=discord.Embed(title="HELP", description="Available commands", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805196091351498802/815948710559088651/fototapeten-note-note-musicali-pentagramma-musik.png")
        embed.add_field(name="~join", value="Join Discord voice channel", inline=True)
        embed.add_field(name="~p url", value="play Music", inline=False)
        embed.add_field(name="~leave", value="leave Discord voice channel", inline=False)
        embed.add_field(name="~stop", value="Stop Music", inline=False)
        embed.add_field(name="~resum", value="Plays paused music again", inline=False)
        await message.channel.send(embed=embed)

client.run(token)


