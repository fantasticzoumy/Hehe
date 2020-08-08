import discord
import asyncio
from discord.ext import commands
from asyncio import sleep
from discord.ext.commands import has_permissions


client = commands.Bot(command_prefix="he!")

async def on_ready():
    print("Beep Boop Bot Is Ready XD")

@client.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong :ping_pong: {round(client.latency * 1000)}ms")

@client.event
async def on_message(message):
    await client.process_commands(message)
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello Hehe:)")

@client.command(name="clear", help="Clear some messages away.", aliases=["delmsgs"], usage="[number of messages to delete (5)]")
@has_permissions(manage_messages=True)
async def clear(ctx, msgcount: int=10):
        await ctx.channel.purge(
            limit=msgcount + 1
        )
        report = await ctx.send(f"""{msgcount} (probably) messages deleted.""")
        await sleep(3)
        await report.delete()

@client.command(name="purge", help="Purge a channel of everything.", aliases=["wipe", "wipechannel"])
@has_permissions(manage_channels=True)
async def purge(ctx):
    newchannel = await ctx.channel.clone(reason=f"Purging #{ctx.channel.name}")
    await newchannel.edit(position=ctx.channel.position, reason=f"Purging #{ctx.channel.name}")
    await ctx.channel.delete(reason=f"Purged #{ctx.channel.name}")

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
     await member.ban(reason=reason)

client.run('TOKEN')
