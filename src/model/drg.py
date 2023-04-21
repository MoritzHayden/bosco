from enum import Enum, auto
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
    SANDBLASTED_CORRIDORS = auto()

    def __str__(self):
        return to_title_case(self.name)


class Anomaly(Enum):
    CRITICAL_WEAKNESS = auto()
    DOUBLE_XP = auto()
    GOLDEN_BUGS = auto()
    GOLD_RUSH = auto()
    LOW_GRAVITY = auto()
    MINERAL_MANIA = auto()
    RICH_ATMOSPHERE = auto()
    VOLATILE_GUTS = auto()

    def __str__(self):
        return to_title_case(self.name)


class Warning(Enum):
    CAVE_LEECH_CLUSTER = auto()
    ELITE_THREAT = auto()
    EXPLODER_INFESTATION = auto()
    HAUNTED_CAVE = auto()
    LETHAL_ENEMIES = auto()
    LITHOPHAGE_OUTBREAK = auto()
    LOW_OXYGEN = auto()
    MACTERA_PLAGUE = auto()
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
                 anomaly: Anomaly,
                 warning: Warning):
        self.stage: int = stage
        self.primary: str = primary
        self.secondary: str = secondary
        self.anomaly: Anomaly = anomaly
        self.warning: Warning = warning

    def __str__(self):
        return ""


class DeepDive:
    def __init__(self,
                 type: DeepDiveType,
                 name: str,
                 biome: Biome,
                 date: str,
                 url: str,
                 stages: list[DeepDiveStage]):
        self.type: DeepDiveType = type
        self.name: str = name
        self.biome: Biome = biome
        self.date: str = date
        self.url: str = url
        self.stages: list[DeepDiveStage] = stages

    def __str__(self):
        return f'{str(self.type)} | {self.name} | {str(self.biome)}'
