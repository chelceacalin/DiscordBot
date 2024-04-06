import discord
from discord.ext import commands


async def sendMessageOnChannel(member: discord.Member, channel_name: str, message: str, message_type: str):
    guild: discord.Guild = member.guild
    for channel in guild.channels:
        if channel.name.lower() == channel_name:
            if message_type == "channel":
                await channel.send(message)
            else:
                await member.send(message)
            break


async def on_member_join(member: discord.Member) -> None:
    await sendMessageOnChannel(member, "bine_ai_venit", 'Welcome, {}'.format(member), "channel")


async def on_member_remove(member: discord.Member) -> None:
    await sendMessageOnChannel(member, "general", f'{member} has decided to leave us :(', "channel")
