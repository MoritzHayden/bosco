from enum import Enum
from typing import Optional
import emoji
from pydantic import BaseModel


class Type(str, Enum):
    ALL = "All"
    DEEP_DIVE = "Deep Dive"
    ELITE_DEEP_DIVE = "Elite Deep Dive"


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
    OSSUARY_DEPTHS = "Ossuary Depths"


class Anomaly(str, Enum):
    BLOOD_SUGAR = "Blood Sugar"
    CRITICAL_WEAKNESS = "Critical Weakness"
    DOUBLE_XP = "Double XP"
    GOLD_RUSH = "Gold Rush"
    GOLDEN_BUGS = "Golden Bugs"
    LOW_GRAVITY = "Low Gravity"
    MINERAL_MANIA = "Mineral Mania"
    RICH_ATMOSPHERE = "Rich Atmosphere"
    SECRET_SECONDARY = "Secret Secondary"
    VOLATILE_GUTS = "Volatile Guts"
    PIT_JAW_COLONY = "Pit Jaw Colony"
    SCRAB_NESTING_GROUNDS = "Scrab Nesting Grounds"


class Warning(str, Enum):
    CAVE_LEECH_CLUSTER = "Cave Leech Cluster"
    DUCK_AND_COVER= "Duck and Cover"
    EBONITE_OUTBREAK = "Ebonite Outbreak"
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


class Stage(BaseModel):
    id: int
    primary: str
    secondary: str
    anomaly: Optional[Anomaly]
    warning: Optional[Warning]

    def __str__(self):
        content = emoji.emojize(f':bullseye: {self.primary}\n')
        content += emoji.emojize(f':bullseye: {self.secondary}\n')
        content += emoji.emojize(
            f':warning: {self.anomaly.value if self.anomaly else "None"}\n'
        )
        content += emoji.emojize(
            f':police_car_light: {self.warning.value if self.warning else "None"}'
        )
        return content


class Variant(BaseModel):
    type: Type
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

    def get_variant(self, type: Type) -> Variant:
        for variant in self.variants:
            if variant.type == type:
                return variant
        return None
