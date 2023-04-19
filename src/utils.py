import json


# Get a list of authorized users (admins)
def get_admins():
    admins = []
    with open("admins.json") as f:
        data = json.load(f)
        for admin in data['admins']:
            admins.append(str(admin["id"]))
    return admins
