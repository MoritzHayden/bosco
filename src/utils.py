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
    for admin_id in get_admin_ids():
        if id == admin_id:
            return True
    return False
