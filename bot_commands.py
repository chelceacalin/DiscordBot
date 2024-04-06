from discord.ext import commands
import random


@commands.command()
async def hello(ctx: commands.Context):
    await ctx.send(f'Hello {ctx.author}')


@commands.command(name='dice')
async def dice(ctx: commands.Context):
    await ctx.send(f'You have rolled {str(random.randint(1, 6))}')


