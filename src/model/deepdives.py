from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict
from util.emoji import get_emoji

class DiveVariant(str, Enum):
    ALL = "All"
    DEEP_DIVE = "Deep Dive"
    ELITE_DEEP_DIVE = "Elite Deep Dive"

class MissionType(str, Enum):
    MINING_EXPEDITION = "Mining Expedition"
    EGG_HUNT = "Egg Hunt"
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

class Mission():
    """ Represents one mission objective like collect 7 Aquarq or mine 200 Morkite"""
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    def emoji(self) -> str:
        return get_emoji(self.type)

    @property
    def type(self) -> Optional[MissionType]:
        """Mission types provided by API don't have much overlap with regular
        mission types thus, there needs to be such conversion"""

        type_name_matrix: dict[str, MissionType] = {
            'morkite': MissionType.MINING_EXPEDITION,
            'egg':  MissionType.EGG_HUNT,
            'refining': MissionType.ON_SITE_REFINING,
            'mule': MissionType.SALVAGE_OPERATION,
            'aquarq': MissionType.POINT_EXTRACTION,
            'escort':  MissionType.ESCORT_DUTY,
            'dreadnought': MissionType.ELIMINATION,
            'black box':  MissionType.BLACK_BOX,
            'sabotage':  MissionType.INDUSTRIAL_SABOTAGE
        }

        for (name, type) in type_name_matrix.items():
            if name in self.name.lower():
                return type

        return None

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


class Variant(BaseModel):
    type: DiveVariant
    name: str
    biome: Biome
    seed: int
    stages: list[Stage]

    def get_stage(self, id: int) -> Optional[Stage]:
        for stage in self.stages:
            if stage.id == id:
                return stage
        return None


class DeepDives(BaseModel):
    startTime: str
    endTime: str
    variants: list[Variant]

    def get_variant(self, type: DiveVariant) -> Variant:
        for variant in self.variants:
            if variant.type == type:
                return variant
        return self.variants[0]
