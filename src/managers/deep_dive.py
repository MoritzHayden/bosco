from logging import Logger
from typing import List
import discord
from service.drg import DRGService
from model.deepdives import DiveVariant, Mission, Stage, Variant
from util.date import prettify_datetime
from util.emoji import get_emoji
from util.constants import DEEP_DIVE_IMAGE_URL


class DeepDiveManager():
    def __init__(self, logger: Logger, drg_service: DRGService):
        self.logger: Logger = logger.getChild('DeepDiveManager')
        self.drg_service: DRGService = drg_service

    def get_embed(self, dive_variant: DiveVariant, skip_custom_emojis = False):
        deep_dives = self.drg_service.get_deepdives()

        start_date = prettify_datetime(deep_dives.startTime)
        embed = discord.Embed(
            title=f'Weekly Deep Dives ({start_date})',
            color=0xFDA50F
        )
        embed.set_thumbnail(url=DEEP_DIVE_IMAGE_URL)

        if skip_custom_emojis:
            embed.description = self.get_custom_emojis_notice()

        included_types = self.get_included_variants(dive_variant)

        for type in included_types:
            variant: Variant = deep_dives.get_variant(type)
            embed.add_field(
                name=self.generate_variant_header(variant),
                value='',
                inline=False
            )
            for stage in variant.stages:
                embed.add_field(
                    name=f'Stage {stage.id}',
                    value=self.generate_stage_details(stage, skip_custom_emojis),
                    inline=True
                )

        return embed

    def get_custom_emojis_notice(self):
        return (
            '>>> :information_source: **Attention Miners!**\n' +
            'Deep Dive embed have been update to use new custom emojis! Please ' +
            'enable `Use External Emojis` permission for Bosco\'s role to enable ' +
            'this feature.'
        )

    def get_included_variants(self, input: DiveVariant) -> List[DiveVariant]:
        if input is DiveVariant.ALL:
            return [ DiveVariant.DEEP_DIVE, DiveVariant.ELITE_DEEP_DIVE]
        return [ input ]

    def generate_variant_header(self, variant: Variant):
        return f'{str(variant.type.value)} | {variant.name} | {str(variant.biome.value)}'

    def generate_mission_header(self, mission: Mission, skip_custom_emojis = False):
        emoji = ':dart:' if skip_custom_emojis else get_emoji(mission.type)
        return f'{emoji} {mission.name}'

    def generate_stage_details(self, stage: Stage, skip_custom_emojis = False):
        result = f'{self. generate_mission_header(stage.primary, skip_custom_emojis)}\n'
        result += f'{self.generate_mission_header(stage.secondary, skip_custom_emojis)}\n'
        if stage.anomaly:
            emoji = ':warning:' if skip_custom_emojis else get_emoji(stage.anomaly)
            result += f'{emoji} {stage.anomaly.value}\n'
        if stage.warning:
            emoji = ':rotating_light:' if skip_custom_emojis else get_emoji(stage.warning)
            result += f'{emoji} {stage.warning.value}\n'
        return result
