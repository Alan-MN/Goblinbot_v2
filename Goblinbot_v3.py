import discord
from discord.ext import commands
from musica import Musica
client = commands.Bot(command_prefix="?")
token = open('token.txt','r')


@client.command(aliases=['p'])
async def play(ctx, url: str):
    botinvc = ctx.guild.me.voice
    if ctx.author.voice and ctx.author.voice.channel:
        canal_voz = ctx.author.voice.channel
    else:
        await ctx.send('você precisa estar em um canal de voz para tocar música')
        return
    if not botinvc:
        await canal_voz.connect()
    musica = Musica(url)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(musica.True_url))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1
    await ctx.send(f'Tocando agora: {musica.nome}')


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


@client.command(aliases =['st'])
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(aliases = ['sk'])
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.skip()

client.run(token.read())