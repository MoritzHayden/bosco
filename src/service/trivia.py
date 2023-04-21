import random


class TriviaService:
    def __init__(self):
        self.trivia: list[str] = [
            'Deep Dives were added in the September 26th, 2019 update.',
            'The name of the first ever Deep Dive mission was "Hard Blade".'
        ]

    def get_random_trivia(self):
        return random.choice(self.trivia)
