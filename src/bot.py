import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import utils

# Initialize environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Ready event
@client.event
async def on_ready():
    print("Bot Ready!")

# Sync command
@tree.command(name = "sync",
              description = "Admin: Syncs the command tree")
async def first_command(ctx):
    if ctx.user.id in utils.get_admins():
        await tree.sync()
        await ctx.response.send_message("Successfully synced command tree.")
    else:
        await ctx.response.send_message("Sorry, only admins can run this command.")

# Ping command
@tree.command(name = "ping",
              description = "Pings the bot and returns latency")
async def first_command(ctx):
    await ctx.response.send_message(f'Pong! Latency: {round(client.latency*1000)}ms')

# Deep Dives command
@tree.command(name = "deep-dives",
              description = "Returns details about the weekly deep dives")
async def first_command(ctx):
    await ctx.response.send_message(f'Coming soon!')

# Fun Fact command
@tree.command(name = "fun-fact",
              description = "Returns one or more fun facts")
async def first_command(ctx, count=1):
    await ctx.response.send_message(f'Coming soon!')

# Run client
client.run(TOKEN)
