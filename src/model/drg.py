from enum import Enum, auto
import emoji
from util.string import to_title_case


class Dwarf(Enum):
    DRILLER = auto()
    ENGINEER = auto()
    GUNNER = auto()
    SCOUT = auto()

    def __str__(self):
        return to_title_case(self.name)


class DeepDiveType(Enum):
    ALL = auto()
    DEEP_DIVE = auto()
    ELITE_DEEP_DIVE = auto()

    def __str__(self):
        return to_title_case(self.name)


class Biome(Enum):
    AZURE_WEALD = auto()
    CRYSTALLINE_CAVERNS = auto()
    DENSE_BIOZONE = auto()
    FUNGUS_BOGS = auto()
    GLACIAL_STRATA = auto()
    HOLLOW_BOUGH = auto()
    MAGMA_CORE = auto()
    RADIOACTIVE_EXCLUSION_ZONE = auto()
    SALT_PITS = auto()
    SALTS_PIT = auto() # Needed for Reddit post typo
    SANDBLASTED_CORRIDORS = auto()

    def __str__(self):
        return to_title_case(self.name)


class AnomalyMutator(Enum):
    CRITICAL_WEAKNESS = auto()
    DOUBLE_XP = auto()
    GOLDEN_BUGS = auto()
    GOLD_RUSH = auto()
    LOW_GRAVITY = auto()
    MINERAL_MANIA = auto()
    NONE = auto()
    RICH_ATMOSPHERE = auto()
    VOLATILE_GUTS = auto()

    def __str__(self):
        return to_title_case(self.name)


class WarningMutator(Enum):
    CAVE_LEECH_CLUSTER = auto()
    ELITE_THREAT = auto()
    EXPLODER_INFESTATION = auto()
    HAUNTED_CAVE = auto()
    LETHAL_ENEMIES = auto()
    LITHOPHAGE_OUTBREAK = auto()
    LOW_OXYGEN = auto()
    MACTERA_PLAGUE = auto()
    NONE = auto()
    PARASITES = auto()
    REGENERATIVE_BUGS = auto()
    RIVAL_PRESENCE = auto()
    SHIELD_DISRUPTION = auto()
    SWARMAGEDDON = auto()

    def __str__(self):
        return to_title_case(self.name)


class DeepDiveStage:
    def __init__(self,
                 stage: int,
                 primary: str,
                 secondary: str,
                 anomaly: AnomalyMutator,
                 warning: WarningMutator):
        self.stage: int = stage
        self.primary: str = primary
        self.secondary: str = secondary
        self.anomaly: AnomalyMutator = anomaly
        self.warning: WarningMutator = warning

    def __str__(self):
        content = emoji.emojize(f':bullseye: {self.primary}\n')
        content += emoji.emojize(f':bullseye: {self.secondary}\n')
        content += emoji.emojize(f':warning: {self.anomaly}\n')
        content += emoji.emojize(f':police_car_light: {self.warning}')
        return content


class DeepDive:
    def __init__(self,
                 dive_type: DeepDiveType,
                 name: str,
                 biome: Biome,
                 date: str,
                 url: str,
                 stages: list[DeepDiveStage]):
        self.dive_type: DeepDiveType = dive_type
        self.name: str = name
        self.biome: Biome = biome
        self.date: str = date
        self.url: str = url
        self.stages: list[DeepDiveStage] = stages

    def __str__(self):
        return f'{str(self.dive_type)} | {self.name} | {str(self.biome)}'
