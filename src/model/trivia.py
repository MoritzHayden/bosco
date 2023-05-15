import random
from pydantic import BaseModel


class Trivia(BaseModel):
    trivia: list[str]

    def get_random_trivia(self) -> str:
        return random.choice(self.trivia)

    def get_trivia_at(self, index: int) -> str:
        return self.trivia[index]
