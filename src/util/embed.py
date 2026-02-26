import discord

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
