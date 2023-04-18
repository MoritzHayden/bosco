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

@client.event
async def on_ready():
    print("Bot Ready!")

# Sync command
@tree.command(name = "sync", description = "Syncs the command tree (admin only)")
async def first_command(ctx):
    print(utils.get_admins())
    if ctx.user.id in utils.get_admins():
        await tree.sync()
        await ctx.response.send_message("Synced command tree!")
    else:
        await ctx.response.send_message("Error: Only admins can run this command!")

# Ping command
@tree.command(name = "ping", description = "Pings the bot and returns latency")
async def first_command(ctx):
    print('Pong! Latency: {0}'.format(round(client.latency, 1)))
    await ctx.response.send_message('Pong! Latency: {0}'.format(round(client.latency, 1)))

client.run(TOKEN)
