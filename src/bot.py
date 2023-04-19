import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from dwarf import Dwarf
from deep_dive_type import DeepDiveType
from api_ninjas import get_fun_facts
from utils import get_random_salute


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


# Help command
@tree.command(name="help",
              description="Get help with Bosco")
async def help(ctx):
    print('INFO: Recieved /help command')
    embed_message = discord.Embed(title="Bosco Help", url="https://boscobot.dev/", color=0xFDA50F)
    embed_message.add_field(name="/help", value="Get help with Bosco", inline=False)
    embed_message.add_field(name="/ping", value="Ping Bosco", inline=False)
    embed_message.add_field(name="/deep-dive", value="Get details about the weekly deep dives", inline=False)
    embed_message.add_field(name="/loadout", value="Get a randomized loadout for the specified Dwarf", inline=False)
    embed_message.add_field(name="/rock-and-stone", value="Rock and Stone!", inline=False)
    embed_message.add_field(name="/fun-fact", value="Get one or more fun facts", inline=False)
    await ctx.response.send_message(embed=embed_message)
    print('SUCCESS: Processed /help command')


# Ping command
@tree.command(name="ping",
              description="Ping Bosco")
async def ping(ctx):
    print('INFO: Recieved /ping command')
    latency = round(client.latency*1000)
    await ctx.response.send_message(f'Pong! Latency: {latency}ms')
    print(f'SUCCESS: Processed /ping command with latency={latency}ms')


# Deep Dive command
@tree.command(name="deep-dive",
              description="Get details about the weekly deep dives")
@app_commands.describe(type="Which Deep Dive(s) to get details for")
async def deep_dive(ctx, type: DeepDiveType = DeepDiveType.ALL):
    print(f'INFO: Recieved /deep-dive command with type={type.name}')
    await ctx.response.send_message('Coming soon!')
    print('SUCCESS: Processed /deep-dive command')


# Loadout command
@tree.command(name="loadout",
              description="Get a randomized loadout for the specified Dwarf")
@app_commands.describe(dwarf="Which Dwarf to generate a loadout for")
async def loadout(ctx, dwarf: Dwarf):
    print(f'INFO: Recieved /loadout command with dwarf={dwarf.name}')
    await ctx.response.send_message('Coming soon!')
    print('SUCCESS: Processed /loadout command')


# Rock and Stone command
@tree.command(name="rock-and-stone",
              description="Rock and Stone!")
async def rock_and_stone(ctx):
    print(f'INFO: Recieved /rock-and-stone command')
    await ctx.response.send_message(get_random_salute())
    print('SUCCESS: Processed /rock-and-stone command')


# Fun Fact command
@tree.command(name="fun-fact",
              description="Get one or more fun facts")
@app_commands.describe(count="Number of fun facts to return (1-10)")
async def fun_facts(ctx, count: int = 1):
    print(f'INFO: Recieved /fun-fact command with count={count}')
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
            print('SUCCESS: Processed /fun-fact command')
        else:
            await ctx.response.send_message('Oops, something went wrong! Please try again later.')
            print('FAILURE: Failed to process /fun-fact command')
    else:
        print('FAILURE: Failed to process /fun-fact command')
        await ctx.response.send_message('Oops, please try again with a `count` in range of 1-10.')

# Run client
client.run(DISCORD_TOKEN)
