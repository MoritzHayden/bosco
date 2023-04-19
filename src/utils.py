import os
import json
import random


# Return a random salute string
def get_random_salute():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'json/salutes.json')
    with open(filename) as f:
        data = json.load(f)
        return random.choice(data['salutes'])
