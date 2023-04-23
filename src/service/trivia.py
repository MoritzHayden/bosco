import os
import json
import random


class TriviaService:
    def __init__(self):
        self.trivia: list[str] = self.__populate_trivia()

    def get_random_trivia(self):
        return random.choice(self.trivia)

    def get_trivia(self, index: int) -> str:
        return self.trivia[index]

    def __populate_trivia(self) -> list[str]:
        filename = os.path.join(os.path.dirname(__file__), '../json/trivia.json')
        with open(file=filename, encoding="utf-8") as f:
            return json.load(f)['trivia']
