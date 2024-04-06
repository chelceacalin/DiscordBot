import discord
from discord.ext import commands


@commands.command(pass_context=True)
async def join(ctx: commands.Context):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not connected to a voice channel.")
    pass


@commands.command(pass_context=True)
async def leave(ctx: commands.Context):
    try:
        if ctx.author.voice:
            await ctx.guild.voice_client.disconnect(force=True)
            await ctx.send("I left the voice chat")
        else:
            await ctx.send("I am not connected to a voice channel.")
    except Exception:
        await ctx.send("I am not connected to a voice channel.")\

