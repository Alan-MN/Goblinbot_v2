import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="?")
token = 'insira o token do bot aqui'


@client.command(aliases=['p'])
async def play(ctx, url: str):
    botinvc = ctx.guild.me.voice
    song_there = os.path.isfile('song.webm')
    queue = [url]
    try:
        if song_there:
            os.remove('song.webm')
    except PermissionError:
        await ctx.send('adicionei a musica na fila')
        queue.append(url)
        return

    voicechannel = discord.utils.get(ctx.guild.voice_channels, name='BADERNA')
    if not botinvc:
        await voicechannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': '249/250/251',
    }
    name = ""
    while len(queue)>0:
        link_muisca = queue.pop(0)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link_muisca])
        for file in os.listdir('./'):
            if file.endswith('.webm'):
                for i in range(len(file.split('.'))):
                    if file.split('.')[i] !='webm':
                        name = name + file.split('.')[i]
                os.rename(file, 'song.webm')

        voice.play(discord.FFmpegOpusAudio(executable='C:/FFMPEG/ffmpeg.exe', source='song.webm'))
        await ctx.send(f'Tocando agora: {name}')


@client.command(aliases=['l'])
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.skip()


client.run(token)