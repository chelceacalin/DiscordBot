import requests
import json
from discord.ext import commands
from typing import List, Dict

Quote = Dict[str, str]


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote: Quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


@commands.command(name="inspire")
async def inspire(ctx: commands.Context):
    await send_quote(ctx.message.channel)


@commands.command(name="inspire?")
async def inspirePrivate(ctx: commands.Context):
    await send_quote(ctx.message.author)


async def send_quote(destination):
    quote: Quote = get_quote()
    await destination.send(quote)
