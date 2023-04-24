import os
import json
import random


class SaluteService:
    def __init__(self):
        self.salutes: list[str] = self.__populate_salutes()

    def get_random_salute(self) -> str:
        return random.choice(self.salutes)

    def get_salute(self, index: int) -> str:
        return self.salutes[index]

    def __populate_salutes(self) -> list[str]:
        filename = os.path.join(os.path.dirname(__file__), '../json/salutes.json')
        with open(file=filename, encoding="utf-8") as f:
            return json.load(f)['salutes']
