from enum import Enum
from typing import Optional, Union
import emoji
from pydantic import BaseModel, ConfigDict, field_validator


class DiveType(str, Enum):
    ALL = "All"
    DEEP_DIVE = "Deep Dive"
    ELITE_DEEP_DIVE = "Elite Deep Dive"

class MissionType(str, Enum):
    MINING_EXPEDITION = "Mining Expedition"
    EGG_HUNT ="Egg Hunt"
    ON_SITE_REFINING = "On-Site Refining"
    SALVAGE_OPERATION = "Salvage Operation"
    POINT_EXTRACTION = "Point Extraction"
    ESCORT_DUTY = "Escort Duty"
    ELIMINATION = "Elimination"
    BLACK_BOX = "Black Box"
    INDUSTRIAL_SABOTAGE = "Industrial Sabotage"


class Biome(str, Enum):
    CRYSTALLINE_CAVERNS = "Crystalline Caverns"
    SALT_PITS = "Salt Pits"
    FUNGUS_BOGS = "Fungus Bogs"
    RADIOACTIVE_EXCLUSION_ZONE = "Radioactive Exclusion Zone"
    DENSE_BIOZONE = "Dense Biozone"
    GLACIAL_STRATA = "Glacial Strata"
    HOLLOW_BOUGH = "Hollow Bough"
    AZURE_WEALD = "Azure Weald"
    MAGMA_CORE = "Magma Core"
    SANDBLASTED_CORRIDORS = "Sandblasted Corridors"


class Anomaly(str, Enum):
    CRITICAL_WEAKNESS = "Critical Weakness"
    DOUBLE_XP = "Double XP"
    GOLD_RUSH = "Gold Rush"
    GOLDEN_BUGS = "Golden Bugs"
    LOW_GRAVITY = "Low Gravity"
    MINERAL_MANIA = "Mineral Mania"
    RICH_ATMOSPHERE = "Rich Atmosphere"
    VOLATILE_GUTS = "Volatile Guts"


class Warning(str, Enum):
    CAVE_LEECH_CLUSTER = "Cave Leech Cluster"
    ELITE_THREAT = "Elite Threat"
    EXPLODER_INFESTATION = "Exploder Infestation"
    HAUNTED_CAVE = "Haunted Cave"
    LETHAL_ENEMIES = "Lethal Enemies"
    LOW_OXYGEN = "Low Oxygen"
    MACTERA_PLAGUE = "Mactera Plague"
    PARASITES = "Parasites"
    REGENERATIVE_BUGS = "Regenerative Bugs"
    RIVAL_PRESENCE = "Rival Presence"
    SHIELD_DISRUPTION = "Shield Disruption"
    SWARMAGEDDON = "Swarmageddon"

""" Represents one mission objective like collect 7 Aquarq or mine 200 Morkite"""
class Mission():
    name: str;

    def __init__(self, name: str):
        self.name = name

    @property
    def emoji(self) -> str:
        return get_emoji(self.type)

    @property
    def type(self) -> MissionType:
        """Mission types provided by API don't have much overlap with regular
        mission types thus, there needs to be such conversion"""
        if(self.name.startswith('Morkite')):
            return MissionType.MINING_EXPEDITION;
        elif(self.name.startswith('Egg')):
            return MissionType.EGG_HUNT;
        elif(self.name.startswith('On-Site Refining')):
            return MissionType.ON_SITE_REFINING;
        elif(self.name.startswith('Mule')):
            return MissionType.SALVAGE_OPERATION;
        elif(self.name.startswith('Aquarq')):
            return MissionType.POINT_EXTRACTION;
        elif(self.name.startswith('Escort Duty')):
            return MissionType.ESCORT_DUTY;
        elif(self.name.startswith('Dreadnought')):
            return MissionType.ELIMINATION;
        elif(self.name.startswith('Black Box')):
            return MissionType.BLACK_BOX;
        elif(self.name.startswith('Industrial Sabotage')):
            return MissionType.INDUSTRIAL_SABOTAGE;
        else:
            raise ValueError(f'Invalid mission name: {self.name}')
    
    def __str__(self):
        return f'{self.emoji} {self.name}'



class Stage(BaseModel):
    id: int
    primary: Mission
    secondary: Mission
    anomaly: Optional[Anomaly]
    warning: Optional[Warning]

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(self, **kwargs):
        kwargs['primary'] = Mission(kwargs['primary'])
        kwargs['secondary'] = Mission(kwargs['secondary'])
        super().__init__(**kwargs)

    def __str__(self):
        content = f'{self.primary}\n'
        content += f'{self.secondary}\n'
        if(self.anomaly):
            content += f'{get_emoji(self.anomaly)} {self.anomaly.value}\n'
        if(self.warning):
            content += f'{get_emoji(self.warning)} {self.warning.value}\n'
        return content


class Variant(BaseModel):
    type: DiveType
    name: str
    biome: Biome
    seed: int
    stages: list[Stage]

    def get_stage(self, id: int) -> Stage:
        for stage in self.stages:
            if stage.id == id:
                return stage
        return None

    def __str__(self):
        return f'{str(self.type.value)} | {self.name} | {str(self.biome.value)}'


class DeepDives(BaseModel):
    startTime: str
    endTime: str
    variants: list[Variant]

    def get_variant(self, type: DiveType) -> Variant:
        for variant in self.variants:
            if variant.type == type:
                return variant
        return None

def get_emoji(model: Union[MissionType, Warning, Anomaly]) -> str:
    if isinstance(model, MissionType):
        return "🎯"
    elif isinstance(model, Warning):
        return "⚠️"
    else:
        return "🚨"