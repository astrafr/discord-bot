import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@commands.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'Cleared {amount} messages', delete_after=5)

@commands.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, time: int, *, reason=None):
    duration = discord.utils.utcnow() + discord.timedelta(seconds=time)
    await member.timeout(until=duration, reason=reason)
    await ctx.send(f'Timed out {member.mention} for {time} seconds')

@commands.command()
@commands.has_permissions(moderate_members=True)
async def untimeout(ctx, member: discord.Member):
    await member.timeout(until=None)
    await ctx.send(f'Untimed out {member.mention}')
