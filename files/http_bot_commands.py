import asyncio
import json
import os
from typing import Dict

import openai
import requests
from discord.ext import commands

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


openai.api_key = os.getenv("OPENAI_API_KEY")


@commands.command()
async def question(ctx: commands.Context, *, question_text: str):
    async with ctx.typing():
        await asyncio.sleep(2)  # Simulate typing for 2 seconds
        ans: str = chat_with_gpt(question_text)
        if len(ans) < 1:
            await ctx.send("There was an error. Please try again.")
        else:
            await ctx.send(ans)


def chat_with_gpt(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(e)
    return ""
