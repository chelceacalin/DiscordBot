import os

from discord import Intents
from bot_commands import *
from http_bot_commands import *

intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Bot is ready')


# Bot Commands
client.add_command(hello)
client.add_command(dice)

# Http Bot Commands
client.add_command(inspire)
client.add_command(inspirePrivate)


client.run(os.getenv('DISCORD_TOKEN'))
