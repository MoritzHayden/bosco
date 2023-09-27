import discord
from model.deepdives import DeepDives, DiveType, Variant
from util.date import prettify_datetime


def embed_deep_dive(thumbnail: discord.File, deep_dives: DeepDives, type: DiveType):
    start_date = prettify_datetime(deep_dives.startTime)
    embed = discord.Embed(title=f'Weekly Deep Dives ({start_date})', color=0xFDA50F)
    embed.set_thumbnail(url=f'attachment://{thumbnail.filename}')

    # Deep Dive
    if type in (type.ALL, type.DEEP_DIVE):
        dd: Variant = deep_dives.get_variant(DiveType.DEEP_DIVE)
        embed.add_field(name=str(dd), value='', inline=False)
        for stage in dd.stages:
            embed.add_field(name=f'Stage {str(stage.id)}', value=str(stage), inline=True)

    # Elite Deep Dive
    if type in (type.ALL, type.ELITE_DEEP_DIVE):
        edd: Variant = deep_dives.get_variant(DiveType.ELITE_DEEP_DIVE)
        embed.add_field(name=str(edd), value='', inline=False)
        for stage in edd.stages:
            embed.add_field(name=f'Stage {str(stage.id)}', value=str(stage), inline=True)

    return embed


def embed_trivia(trivia: str):
    embed = discord.Embed(color=0xFDA50F)
    embed.add_field(name='Did You Know?', value=trivia, inline=False)
    return embed


def embed_help():
    embed = discord.Embed(title="Bosco Help", url="https://boscobot.dev/", color=0xFDA50F)
    embed.add_field(name="/ping", value="Ping Bosco and get latency", inline=False)
    embed.add_field(name="/deep-dive", value="Get weekly Deep Dive details", inline=False)
    embed.add_field(name="/rock-and-stone", value="You already know what this does", inline=False)
    embed.add_field(name="/trivia", value="Get a random piece of DRG trivia", inline=False)
    embed.add_field(name="/invite", value="Invite Bosco to your server", inline=False)
    embed.add_field(name="/help", value="View the command list and helpful links", inline=False)
    return embed
