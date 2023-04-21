import discord
from model.drg import DeepDive, DeepDiveType


def embed_deep_dive(thumbnail: discord.File, deep_dives: list[DeepDive], type: DeepDiveType):
    dd, edd = deep_dives
    embed_message = discord.Embed(title=f'Weekly Deep Dives ({dd.date})', url=dd.url, color=0xFDA50F)
    embed_message.set_thumbnail(url=f'attachment://{thumbnail.filename}')

    # Deep Dive
    if type in (DeepDiveType.ALL, DeepDiveType.DEEP_DIVE):
        embed_message.add_field(name=str(dd), value='', inline=False)
        for stage in dd.stages:
            embed_message.add_field(name=f'Stage {str(stage.stage)}', value=str(stage), inline=True)

    # Spacer
    if type == DeepDiveType.ALL:
        embed_message.add_field(name='\u200b', value='\u200b', inline=False)
        
    # Elite Deep Dive
    if type in (DeepDiveType.ALL, DeepDiveType.ELITE_DEEP_DIVE):
        embed_message.add_field(name=str(edd), value='', inline=False)
        for stage in edd.stages:
            embed_message.add_field(name=f'Stage {str(stage.stage)}', value=str(stage), inline=True)

    return embed_message


def embed_trivia(trivia: str):
    embed_message = discord.Embed(color=0xFDA50F)
    embed_message.add_field(name='Did You Know?', value=trivia, inline=False)
    return embed_message


def embed_help():
    embed_message = discord.Embed(title="Bosco Help", url="https://boscobot.dev/", color=0xFDA50F)
    embed_message.add_field(name="/ping", value="Ping Bosco and get latency", inline=False)
    embed_message.add_field(name="/deep-dive", value="Get weekly Deep Dive details", inline=False)
    embed_message.add_field(name="/rock-and-stone", value="You already know what this does", inline=False)
    embed_message.add_field(name="/trivia", value="Get a random piece of DRG trivia", inline=False)
    embed_message.add_field(name="/invite", value="Invite Bosco to your server", inline=False)
    embed_message.add_field(name="/help", value="View the command list and helpful links", inline=False)
    return embed_message
