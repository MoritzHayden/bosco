import discord
from model.drg import DeepDive, DeepDiveType


# Construct the embed message for the deep-dive command
def create_deep_dive_embed(thumbnail: discord.File, deep_dives: list[DeepDive], type: DeepDiveType):
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


# Construct the embed message for the fun-fact command
def create_fun_fact_embed(facts: list[str]):
    embed_message = discord.Embed(color=0xFDA50F)
    for i, fact in enumerate(facts):
        header = f'Fun Fact #{i + 1}' if len(facts) > 1 else 'Fun Fact'
        embed_message.add_field(name=header, value=fact, inline=False)
    return embed_message


# Construct the embed message for the help command
def create_help_embed():
    embed_message = discord.Embed(title="Bosco Help", url="https://boscobot.dev/", color=0xFDA50F)
    embed_message.add_field(name="/ping", value="Ping Bosco and get latency", inline=False)
    embed_message.add_field(name="/deep-dive", value="Get weekly Deep Dive details", inline=False)
    embed_message.add_field(name="/loadout", value="Get a randomized Dwarf loadout", inline=False)
    embed_message.add_field(name="/rock-and-stone", value="You already know what this does", inline=False)
    embed_message.add_field(name="/fun-fact", value="Get one or more fun facts", inline=False)
    embed_message.add_field(name="/invite", value="Invite Bosco to your server", inline=False)
    embed_message.add_field(name="/help", value="View the command list and helpful links", inline=False)
    return embed_message
