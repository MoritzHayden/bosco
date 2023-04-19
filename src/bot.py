import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from dwarf import Dwarf
from deep_dive import DeepDive
import utils


# Initialize environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Initialize discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Ready event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Deep Rock Galactic'))
    print("Bot Ready!")


# Message event
@client.event
async def on_message(message):
    # Sync command (ADMIN)
    print(f'message.content: {message.content}')
    if message.content.startswith("!sync") and utils.is_admin(str(message.author.id)):
        print('Authorized')
        await tree.sync()
        print(f'post-sync')
        await message.reply("Successfully synced the command tree.")
        print(f'post-reply')
    else:
        print (f'Check 1: {message.content.startswith("!sync")}')
        print (f'Check 2: {utils.is_admin(str(message.author.id))}')
        print('Unauthorized')


# Ping command
@tree.command(name="ping",
              description="Pings the bot and returns latency")
async def ping(ctx):
    await ctx.response.send_message(f'Pong! Latency: {round(client.latency*1000)}ms')


# Deep Dives command
@tree.command(name="deep-dive",
              description="Returns details about the weekly deep dives")
async def deep_dive(ctx, deep_dive: DeepDive = DeepDive.ALL):
    await ctx.response.send_message(f'Coming soon!')


# Loadout command
@tree.command(name="loadout",
              description="Returns a randomized loadout for the specified Dwarf")
async def loadout(ctx, dwarf: Dwarf):
    await ctx.response.send_message(f'Coming soon!')


# Fun Fact command
@tree.command(name="fun-facts",
              description="Returns one or more fun facts")
async def fun_facts(ctx, count: int = 1):
    await ctx.response.send_message(f'Coming soon!')


# Run client
client.run(DISCORD_TOKEN)
