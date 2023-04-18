import json

# Get a list of authorized users (admins)
def get_admins():
    admins = []
    f = open('src/admins.json')
    data = json.load(f)
    for i in data['admins']:
        admins.append(i["id"])
    f.close()
    return admins
