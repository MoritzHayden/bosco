import os
import json
import emoji
import random
import discord
from deep_dive import DeepDive
from deep_dive_type import DeepDiveType


# Return a random salute string
def get_random_salute():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'json/salutes.json')
    with open(filename) as f:
        data = json.load(f)
        return random.choice(data['salutes'])


# Construct the embed message for the deep-dive command
def create_deep_dive_embed(thumbnail: discord.File, deep_dive_details: list[DeepDive], type: DeepDiveType):
    dd = deep_dive_details[0]
    edd = deep_dive_details[1]
    embed_message = discord.Embed(title=f'Weekly Deep Dives ({dd.date})', url=dd.url, color=0xFDA50F)
    embed_message.set_thumbnail(url=f'attachment://{thumbnail.filename}')

    # Deep Dive
    if type in (DeepDiveType.ALL, DeepDiveType.DEEP_DIVE):
        # Header
        embed_message.add_field(name=f'Deep Dive | {dd.name} | {dd.biome}', value='', inline=False)

        # Stages
        for stage in dd.stages:
            dd_stage_info = ""
            dd_stage_info += emoji.emojize(f':bullseye:  {stage[1]}\n')
            dd_stage_info += emoji.emojize(f':bullseye:  {stage[2]}\n')
            dd_stage_info += emoji.emojize(f':warning:  {stage[3]}\n')
            dd_stage_info += emoji.emojize(f':police_car_light:  {stage[4]}')
            embed_message.add_field(name=f'Stage {stage[0]}', value=dd_stage_info, inline=True)

    # Divider Space
    if type == DeepDiveType.ALL:
        embed_message.add_field(name='\u200b', value='\u200b', inline=False)

    # Elite Deep Dive
    if type in (DeepDiveType.ALL, DeepDiveType.ELITE_DEEP_DIVE):
        # Header
        embed_message.add_field(name=f'Elite Deep Dive | {edd.name} | {edd.biome}', value='', inline=False)

        # Stages
        for stage in edd.stages:
            edd_stage_info = ""
            edd_stage_info += emoji.emojize(f':bullseye:  {stage[1]}\n')
            edd_stage_info += emoji.emojize(f':bullseye:  {stage[2]}\n')
            edd_stage_info += emoji.emojize(f':warning:  {stage[3]}\n')
            edd_stage_info += emoji.emojize(f':police_car_light:  {stage[4]}')
            embed_message.add_field(name=f'Stage {stage[0]}', value=edd_stage_info, inline=True)
    
    return embed_message
