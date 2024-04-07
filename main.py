import os

import discord
from discord import Intents

from bot_commands import *
from client_commands import *
from client_events import *
from http_bot_commands import *

# Initialize intents
intents = Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="!helpme for commands"))
    print('Bot is ready to answer ')


# Client Events
client.add_listener(on_member_join)
client.add_listener(on_member_remove)
client.add_listener(on_message)

# Bot Commands
client.add_command(hello)
client.add_command(dice)

# Bot Voice Channel Commands
client.add_command(join)
client.add_command(leave)
client.add_command(kick)
client.add_command(ban)
client.add_command(contact)

# Http Bot Commands
client.add_command(inspire)
client.add_command(inspirePrivate)


# Help Command

@commands.command(name='helpme')
async def helps(ctx: commands.Context):
    with open("commands.txt", "r") as f:
        commands_content = f.read()
        command_lines = commands_content.split('\n')
        embed = discord.Embed(title="Commands", color=discord.Color.blue())

    for line in command_lines:
        command_name, description = line.split(" -- ")
        embed.add_field(name=command_name.strip(), value=description.strip(), inline=False)

    await ctx.send(embed=embed)

# Help
client.add_command(helps)

client.run(os.getenv('DISCORD_TOKEN'))
