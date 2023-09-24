import os
import logging
import discord
from logging import Formatter, FileHandler, Logger
from discord import app_commands, File, Embed, Intents, Client
from dotenv import load_dotenv
from util.constants import ERROR_RESPONSE_TEXT
from model.deepdives import DeepDives, DiveType
from model.ui import ButtonView
from service.drg import DRGService
from util.embed import embed_deep_dive, embed_trivia, embed_help


# Initialize environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Initialize logger
logger: Logger = logging.getLogger('discord').getChild('bot')
logger.setLevel(logging.DEBUG)
logger_formatter: Formatter = logging.Formatter("%(asctime)s %(levelname)s\t%(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")
logger_file_handler: FileHandler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)


# Initialize discord
intents: Intents = discord.Intents.default()
client: Client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Initialize services
drgService = DRGService(logger=logger)


# Ready event
@client.event
async def on_ready():
    logger.info('Readying bot')
    await tree.sync()
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(name='Deep Rock Galactic'))
    logger.info('Bot ready')


# Help command
@tree.command(name="help",
              description="View the command list and helpful links")
async def help_cmd(ctx):
    try:
        logger.info('Recieved /help command')
        await ctx.response.send_message(embed=embed_help(), view=ButtonView())
        logger.info('Processed /help command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        logger.info(f'Failed to process /help command exception={str(e)}')


# Invite command
@tree.command(name="invite",
              description="Invite Bosco to your server")
async def invite_cmd(ctx):
    try:
        logger.info('Recieved /invite command')
        await ctx.response.send_message(view=ButtonView())
        logger.info('Processed /invite command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        logger.error(f'Failed to process /invite command exception={str(e)}')


# Ping command
@tree.command(name="ping",
              description="Ping Bosco and get latency")
async def ping_cmd(ctx):
    try:
        logger.info('Recieved /ping command')
        latency: int = round(client.latency*1000)
        await ctx.response.send_message(f'Pong! Latency: {latency}ms')
        logger.info(f'Processed /ping command with latency={latency}ms')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        logger.error(f'Failed to process /ping command exception={str(e)}')


# Deep Dive command
@tree.command(name="deep-dive",
              description="Get weekly Deep Dive details")
@app_commands.describe(variant="Which Deep Dive(s) to get details for")
async def deep_dive_cmd(ctx, variant: DiveType = DiveType.ALL):
    try:
        logger.info(f'Recieved /deep-dive command with type={variant.name}')
        await ctx.response.defer()
        thumbnail: File = discord.File(fp=os.path.join(os.path.dirname(__file__), 'img/deep-dive.png'),
                                 filename='deep-dive.png')
        deep_dives: DeepDives = drgService.get_deepdives()
        embed_message = embed_deep_dive(thumbnail, deep_dives, variant)
        await ctx.followup.send(file=thumbnail, embed=embed_message)
        logger.info('Processed /deep-dive command')
    except Exception as e:
        await ctx.followup.send(ERROR_RESPONSE_TEXT)
        logger.error(f'Failed to process /deep-dive command exception={str(e)}')


# Rock and Stone command
@tree.command(name="rock-and-stone",
              description="Rock and Stone!")
async def rock_and_stone_cmd(ctx):
    try:
        logger.info('Recieved /rock-and-stone command')
        salute: str = drgService.get_salutes().get_random_salute()
        await ctx.response.send_message(salute)
        logger.info('Processed /rock-and-stone command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        logger.error(f'Failed to process /rock-and-stone command with exception={str(e)}')


# Trivia command
@tree.command(name="trivia",
              description="Get a random piece of DRG trivia.")
async def trivia_cmd(ctx):
    try:
        logger.info('Recieved /trivia command')
        trivia: str = drgService.get_trivia().get_random_trivia()
        embed_message: Embed = embed_trivia(trivia)
        await ctx.response.send_message(embed=embed_message)
        logger.info('Processed /trivia command')
    except Exception as e:
        await ctx.response.send_message(ERROR_RESPONSE_TEXT)
        logger.error(f'Failed to process /trivia command with exception={str(e)}')


# Run client
client.run(DISCORD_TOKEN)
