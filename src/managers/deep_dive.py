from logging import Logger
from typing import List
from service.drg import DRGService
import discord
from model.deepdives import DeepDives, DiveVariant, Mission, Stage, Variant
from util.date import prettify_datetime
from util.emoji import get_emoji


class DeepDiveManager():
    def __init__(self, logger: Logger, drg_service: DRGService):
        self.logger: Logger = logger.getChild('DeepDiveManager')
        self.drg_service: DRGService = drg_service
    
    def get_embed(self, dive_variant: DiveVariant):
        deep_dives = self.drg_service.get_deepdives()

        start_date = prettify_datetime(deep_dives.startTime)
        embed = discord.Embed(title=f'Weekly Deep Dives ({start_date})', color=0xFDA50F)

        included_types = self.get_included_variants(dive_variant)

        for i, type in enumerate(included_types):
            variant: Variant = deep_dives.get_variant(type)
            embed.add_field(
                name=self.generate_variant_header(variant),
                value='',
                inline=False
            )
            for stage in variant.stages:
                embed.add_field(
                    name=f'Stage {stage.id}',
                    value=self.generate_stage_details(stage),
                    inline=True
                )

        return embed

    def get_included_variants(self, input: DiveVariant) -> List[DiveVariant]:
        if input is DiveVariant.ALL:
            return [ DiveVariant.DEEP_DIVE, DiveVariant.ELITE_DEEP_DIVE]
        return [ input ]

    def generate_variant_header(self, variant: Variant): 
        return f'{str(variant.type.value)} | {variant.name} | {str(variant.biome.value)}'
    
    def generate_mission_header(self, mission: Mission):
        return f'{get_emoji(mission.type)} {mission.name}'

    def generate_stage_details(self, stage: Stage):
        result = f'{self. generate_mission_header(stage.primary)}\n'
        result += f'{self.generate_mission_header(stage.secondary)}\n'
        if stage.anomaly:
            result += f'{get_emoji(stage.anomaly)} {stage.anomaly.value}\n'
        if stage.warning:
            result += f'{get_emoji(stage.warning)} {stage.warning.value}\n'
        return result

