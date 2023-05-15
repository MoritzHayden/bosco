import random
from pydantic import BaseModel


class Salutes(BaseModel):
    salutes: list[str]

    def get_random_salute(self) -> str:
        return random.choice(self.salutes)

    def get_salute_at(self, index: int) -> str:
        return self.salutes[index]
