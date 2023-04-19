import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from dwarf import Dwarf
from deep_dive_type import DeepDiveType
from api_ninjas import get_fun_facts


# Initialize environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
API_NINJAS_TOKEN = os.getenv('API_NINJAS_TOKEN')


# Initialize discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Ready event
@client.event
async def on_ready():
    print('INFO: Syncing command tree')
    await tree.sync()
    print('SUCCESS: Synced command tree')
    print('INFO: Updating bot presence')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Deep Rock Galactic'))
    print('SUCCESS: Updated bot presence')
    print('INFO: Bot ready')


# Ping command
@tree.command(name="ping",
              description="Pings the bot and returns latency")
async def ping(ctx):
    print('INFO: Recieved /ping command')
    latency = round(client.latency*1000)
    await ctx.response.send_message(f'Pong! Latency: {latency}ms')
    print(f'SUCCESS: Processed /ping command with latency={latency}ms')


# Deep Dive command
@tree.command(name="deep-dive",
              description="Returns details about the weekly deep dives")
async def deep_dive(ctx, type: DeepDiveType = DeepDiveType.ALL):
    print(f'INFO: Recieved /deep-dive command with type={type.name}')
    await ctx.response.send_message('Coming soon!')
    print('SUCCESS: Processed /deep-dive command')


# Loadout command
@tree.command(name="loadout",
              description="Returns a randomized loadout for the specified Dwarf")
async def loadout(ctx, dwarf: Dwarf):
    print(f'INFO: Recieved /loadout command with dwarf={dwarf.name}')
    await ctx.response.send_message('Coming soon!')
    print('SUCCESS: Processed /loadout command')

# Fun Fact command
@tree.command(name="fun-facts",
              description="Returns one or more fun facts")
async def fun_facts(ctx, count: int = 1):
    print(f'INFO: Recieved /fun-facts command with count={count}')
    if 1 <= count <= 10:
        facts = get_fun_facts(API_NINJAS_TOKEN, count)
        if len(facts) == count:
            facts_message = ""
            for i, fact in enumerate(facts):
                if len(facts) == 1:
                    facts_message += f'**Fun Fact:** {fact}'
                else:
                    facts_message += f'**Fun Fact #{i + 1}:** {fact}\n\n'
            await ctx.response.send_message(facts_message)
            print('SUCCESS: Processed /fun-facts command')
        else:
            await ctx.response.send_message('Oops, something went wrong! Please try again later.')
            print('FAILURE: Failed to process /fun-facts command')
    else:
        print('FAILURE: Failed to process /fun-facts command')
        await ctx.response.send_message('Oops, please try again with a `count` in range of 1-10.')

# Run client
client.run(DISCORD_TOKEN)
