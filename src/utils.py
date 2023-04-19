import json


# Get a list of authorized users (admins)
def get_admin_ids():
    admins = []
    with open("admins.json") as f:
        data = json.load(f)
        for admin in data['admins']:
            admins.append(str(admin["id"]))
    return admins

def is_admin(id: str):
    return id in get_admin_ids()
