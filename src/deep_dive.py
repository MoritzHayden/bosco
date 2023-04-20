from deep_dive_type import DeepDiveType

class DeepDive:
    def __init__(self, type: DeepDiveType, name: str, biome: str, date: str, url: str):
        self.type = type
        self.name = name
        self.biome = biome
        self.date = date
        self.url = url
        self.stages = []
    
    def add_stage(self, stage: int, primary: str, secondary: str, anomaly: str, warning: str):
        self.stages.append([stage, primary, secondary, anomaly, warning])
