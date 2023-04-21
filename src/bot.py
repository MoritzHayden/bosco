import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from model.drg import Dwarf, DeepDiveType
from service.apininjas import APINinjasService
from service.reddit import RedditService
from service.salute import SaluteService
from util.embed import create_help_embed, create_deep_dive_embed, create_fun_fact_embed
from view.button import ButtonView


# Initialize environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
API_NINJAS_TOKEN = os.getenv('API_NINJAS_TOKEN')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')


# Initialize discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Initialize services
apiNinjasService = APINinjasService(API_NINJAS_TOKEN)
redditService = RedditService(client_id=REDDIT_CLIENT_ID,
                              client_secret=REDDIT_CLIENT_SECRET,
                              user_agent='discord:dev.boscobot',
                              check_for_async=False)
saluteService = SaluteService()

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
              description="View the command list and helpful links")
async def help(ctx):
    print('INFO: Recieved /help command')
    embed_message = create_help_embed()
    await ctx.response.send_message(embed=embed_message, view=ButtonView())
    print('SUCCESS: Processed /help command')


# Invite command
@tree.command(name="invite",
              description="Invite Bosco to your server")
async def invite(ctx):
    print('INFO: Recieved /invite command')
    await ctx.response.send_message(view=ButtonView())
    print('SUCCESS: Processed /invite command')


# Ping command
@tree.command(name="ping",
              description="Ping Bosco and get latency")
async def ping(ctx):
    print('INFO: Recieved /ping command')
    latency = round(client.latency*1000)
    await ctx.response.send_message(f'Pong! Latency: {latency}ms')
    print(f'SUCCESS: Processed /ping command with latency={latency}ms')


# Deep Dive command
@tree.command(name="deep-dive",
              description="Get weekly Deep Dive details")
@app_commands.describe(type="Which Deep Dive(s) to get details for")
async def deep_dive(ctx, type: DeepDiveType = DeepDiveType.ALL):
    print(f'INFO: Recieved /deep-dive command with type={type.name}')
    await ctx.response.defer()
    try:
        thumbnail = discord.File(os.path.join(os.path.dirname(__file__), 'img/deep-dive.png'), filename='deep-dive.png')
        deep_dive_details = redditService.get_weekly_deep_dives(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, type)
        embed_message = create_deep_dive_embed(thumbnail, deep_dive_details, type)
        await ctx.followup.send(file=thumbnail, embed=embed_message)
        print('SUCCESS: Processed /deep-dive command')
    except Exception as e:
        await ctx.followup.send('Oops, something went wrong! Please try again later.')
        print(f'Failure: Failed to process /deep-dive command exception={str(e)}')


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
    try:
        salute = saluteService.get_random_salute()
        await ctx.response.send_message(salute)
        print('SUCCESS: Processed /rock-and-stone command')
    except Exception as e:
        await ctx.response.send_message('Oops, something went wrong! Please try again later.')
        print(f'FAILURE: Failed to process /rock-and-stone command with exception={str(e)}')


# Fun Fact command
@tree.command(name="fun-fact",
              description="Get one or more fun facts")
@app_commands.describe(count="Number of fun facts to return (1-5)")
async def fun_facts(ctx, count: app_commands.Range[int, 1, 5] = 1):
    print(f'INFO: Recieved /fun-fact command with count={count}')
    await ctx.response.defer()
    try:
        facts = apiNinjasService.get_facts(API_NINJAS_TOKEN, count)
        embed_message = create_fun_fact_embed(facts)
        await ctx.followup.send(embed=embed_message)
        print('SUCCESS: Processed /fun-fact command')
    except Exception as e:
        await ctx.followup.send('Oops, something went wrong! Please try again later.')
        print(f'FAILURE: Failed to process /fun-fact command with exception={str(e)}')


# Run client
client.run(DISCORD_TOKEN)
