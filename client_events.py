from typing import List

import discord


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
    await sendMessageOnChannel(member, "bine_ai_venit",
                               f'Welcome, {member}, use "!helpme to learn about the available commands"', "channel")


async def on_member_remove(member: discord.Member) -> None:
    await sendMessageOnChannel(member, "general", f'{member} has decided to leave us :(', "channel")


bad_words: List[str] = ["fuck", "damn", "shit", "crap"]


async def on_message(message: discord.Message) -> None:
    if bad_words.__contains__(message.content):
        masked_content = message.content[0] + '*' * max(len(message.content) - 2, 0) + message.content[-1]
        warning_message = f"**Avertisment:** Cuvântul ' {masked_content} ' este interzis în acest server."
        await message.channel.send(warning_message)
