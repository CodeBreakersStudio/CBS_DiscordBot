import config
import discord
import sys
import random
import os
from discord.ext import commands, tasks

if len(sys.argv)>1:
    token = sys.argv[1]
else:
    token = config.DISCORD_BOT_TOKEN

client = commands.Bot(command_prefix=config.DISCORD_BOT_PREFIX)

@client.event
async def on_ready():
    print("Bot working")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{config.DISCORD_BOT_PREFIX}help"))

@client.command()
async def pong(ctx):
    await ctx.send("Ping.")

@client.command()
async def topic(ctx):
    verb = ['ruchać', 'zabijać', 'kochać', 'pisać', 'strzelać']
    noun = ['agata', 'dziecko', 'kobieta', 'człowiek', 'cytryny']
    await ctx.send(f"{verb[random.randint(0, len(verb)-1)]} {noun[random.randint(0, len(noun)-1)]}")

@client.command()
async def ping(ctx):
    responses = [
        "Pong.",
        "Pong!",
        "Pong?"
    ]
    await ctx.send(responses[random.randint(0, 2)])

@client.command(aliases=["reset","restart", "reboot"])
@commands.has_permissions(administrator = True)
async def _reset(ctx):
    await ctx.send("Restartowanie bota")
    await client.close()
    os.system("cls")
    os.system("echo Bot restarting")
    os.system("python bot.py")

client.run(token)