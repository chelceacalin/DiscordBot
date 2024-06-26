import discord
from discord import Member
from discord.ext import commands


@commands.command(pass_context=True)
async def join(ctx: commands.Context) -> None:
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not connected to a voice channel.")
    pass


@commands.command(pass_context=True)
async def leave(ctx: commands.Context) -> None:
    try:
        if ctx.author.voice:
            await ctx.guild.voice_client.disconnect(force=True)
            await ctx.send("I left the voice chat")
        else:
            await ctx.send("I am not connected to a voice channel.")
    except Exception:
        await ctx.send("I am not connected to a voice channel.")


@commands.command(pass_context=True, name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx: commands.Context, member: Member, *, reason=None) -> None:
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked")


@kick.error
async def kick_error(ctx: commands.Context, error) -> None:
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing the permissions to kick members")


@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx: commands.Context, member: Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been banned")


@ban.error
async def ban_error(ctx: commands.Context, error) -> None:
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing the permissions to ban members")


@commands.command(name='contact')
async def contact(ctx: commands.Context) -> None:
    embed: discord.Embed = discord.Embed(title="Contact me", description="Find more about me",
                                         colour=discord.Colour.blue(),
                                         url="https://www.linkedin.com/in/chelceacalin/")
    embed.set_author(name="Chelcea Calin",
                     icon_url="https://media.licdn.com/dms/image/D4D03AQHAmLwKm9oufw/profile-displayphoto"
                              "-shrink_400_400/0/1670312373590?e=1718236800&v=beta&t"
                              "=iWJHkcuEWBa0ydZGpf7HgfZKnR1dzSUfM4VC9w1DnVM")

    await ctx.send(embed=embed)


@commands.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addRole(ctx: commands.Context, user: Member, *, role: discord.Role) -> None:

    print(ctx.author.guild_permissions.administrator)
    if role in user.roles:
        await ctx.send(f"{user.mention} has already {role} role")
    else:
        print('else')
        try:
            await user.add_roles(role)
            await ctx.send(f"{user.mention} has been granted {role} role")
        except Exception as e:
            print(e)


@addRole.error
async def role_error(ctx: commands.Context, error) -> None:
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing the permissions to add roles")
    if isinstance(error, Exception):
        await ctx.send("Something went wrong")


@commands.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removeRole(ctx: commands.Context, user: Member, *, role: discord.Role) -> None:
    if role in user.roles:
        try:
            await user.remove_roles(role)
            await ctx.send(f"{user.mention} has been removed from {role} role")
        except Exception as e:
            print(e)
    else:
        await ctx.send(f"{user.mention} doesn't have {role} role")


@removeRole.error
async def removeRole_error(ctx: commands.Context, error) -> None:
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing the permissions to add roles")
