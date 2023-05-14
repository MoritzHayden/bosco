import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from util.constants import ERROR_RESPONSE_TEXT
from model.deepdives import Type
from model.ui import ButtonView
from service.drg import DRGService
from util.embed import embed_deep_dive, embed_trivia, embed_help


# Initialize environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Initialize discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Initialize services
drgService = DRGService()


# Ready event
@client.event
async def on_ready():
    print('INFO: Readying bot')
    await tree.sync()
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(name='Deep Rock Galactic'))
    print('SUCCESS: Bot ready')


# Help command
@tree.command(name="help",
              description="View the command list and helpful links")
async def help_cmd(ctx):
    try:
        print('INFO: Recieved /help command')
        await ctx.response.send_message(embed=embed_help(), view=ButtonView())
        print('SUCCESS: Processed /help command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        print(f'FAILURE: Failed to process /help command exception={str(e)}')


# Invite command
@tree.command(name="invite",
              description="Invite Bosco to your server")
async def invite_cmd(ctx):
    try:
        print('INFO: Recieved /invite command')
        await ctx.response.send_message(view=ButtonView())
        print('SUCCESS: Processed /invite command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        print(f'FAILURE: Failed to process /invite command exception={str(e)}')


# Ping command
@tree.command(name="ping",
              description="Ping Bosco and get latency")
async def ping_cmd(ctx):
    try:
        print('INFO: Recieved /ping command')
        latency: int = round(client.latency*1000)
        await ctx.response.send_message(f'Pong! Latency: {latency}ms')
        print(f'SUCCESS: Processed /ping command with latency={latency}ms')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        print(f'FAILURE: Failed to process /ping command exception={str(e)}')


# Deep Dive command
@tree.command(name="deep-dive",
              description="Get weekly Deep Dive details")
@app_commands.describe(variant="Which Deep Dive(s) to get details for")
async def deep_dive_cmd(ctx, variant: Type = Type.ALL):
    try:
        print(f'INFO: Recieved /deep-dive command with type={variant.name}')
        await ctx.response.defer()
        thumbnail = discord.File(fp=os.path.join(os.path.dirname(__file__), 'img/deep-dive.png'),
                                 filename='deep-dive.png')
        deep_dives = drgService.get_deepdives()
        embed_message = embed_deep_dive(thumbnail, deep_dives, variant)
        await ctx.followup.send(file=thumbnail, embed=embed_message)
        print('SUCCESS: Processed /deep-dive command')
    except Exception as e:
        await ctx.followup.send(ERROR_RESPONSE_TEXT)
        print(f'FAILURE: Failed to process /deep-dive command exception={str(e)}')


# Rock and Stone command
@tree.command(name="rock-and-stone",
              description="Rock and Stone!")
async def rock_and_stone_cmd(ctx):
    try:
        print('INFO: Recieved /rock-and-stone command')
        salute: str = drgService.get_salutes().get_random_salute()
        await ctx.response.send_message(salute)
        print('SUCCESS: Processed /rock-and-stone command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        print(f'FAILURE: Failed to process /rock-and-stone command with exception={str(e)}')


# Trivia command
@tree.command(name="trivia",
              description="Get a random piece of DRG trivia.")
async def trivia_cmd(ctx):
    try:
        print('INFO: Recieved /trivia command')
        trivia: str = drgService.get_trivia().get_random_trivia()
        embed_message = embed_trivia(trivia)
        await ctx.response.send_message(embed=embed_message)
        print('SUCCESS: Processed /trivia command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        print(f'FAILURE: Failed to process /trivia command with exception={str(e)}')


# Run client
client.run(DISCORD_TOKEN)
