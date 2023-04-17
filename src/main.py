import os
import interactions
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = interactions.Client(token=TOKEN)

@bot.command(
    name="ping",
    description="Pings the bot"
)
async def ping(ctx: interactions.CommandContext):
    await ctx.send("pong")

bot.start()
