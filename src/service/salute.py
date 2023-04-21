import os
import json
import random


class SaluteService:
    def __init__(self):
        pass

    def get_random_salute(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../json/salutes.json')
        with open(filename) as f:
            data = json.load(f)
            return random.choice(data['salutes'])
