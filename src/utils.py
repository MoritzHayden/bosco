import json
import random


# Return a random salute string
def get_random_salute():
    with open("json/salutes.json") as f:
        data = json.load(f)
        return random.choice(data['salutes'])
