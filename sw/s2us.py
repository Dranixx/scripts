import base64

def decode_name(data):
    for i in data['RuneFilter']['Filter']:
        i['Name'] = base64.b64decode(i['Name']).decode("utf-8")
    return data

def encode_name(data):
    for i in data['RuneFilter']['Filter']:
        i['Name'] = base64.b64encode(str.encode(i['Name'])).decode("utf-8")
    return data

def get_rarity(filter):
    if filter["Legend"] == 1:
        return "Legend"
    if filter["Hero"] == 1:
        return "Hero"
    if filter["Rare"] == 1:
        return "Rare"

'''
# Efficiency Slot 2/4/6
eff = {
    "Rare": {
        0: 25,
        1: 92,
        2: 95,
        3: 96
    },
    "Hero": {
        0: 25,
        1: 61,
        2: 71,
        3: 76,
        4: 80
    },
    "Legend":{
        0: 25,
        1: 46,
        2: 56,
        3: 64,
        4: 69,
        5: 71
    }
}
slot = ["Slot2", "Slot4", "Slot6"]
'''


# Efficiency Slot 1/3/5
eff = {
    "Hero": {
        0: 25,
        1: 66,
        2: 75,
        3: 80,
        4: 83
    },
    "Legend":{
        0: 25,
        1: 50,
        2: 60,
        3: 66,
        4: 71,
        5: 73
    }
}
slot = ["Slot1", "Slot3", "Slot5"]


def change_eff(data):
    for i in data['RuneFilter']['Filter']:
        if i[slot[0]] == 1 or i[slot[1]] == 1 or i[slot[2]] == 1:
            rarity = get_rarity(i)
            i["Efficiency"] = eff[rarity][i["Level"]]
    return data

def change_type(data, find, type, val):
    inside = False
    for i in data['RuneFilter']['Filter']:
        name = i['Name']
        if inside and name[0] != '[':
            inside = False
        if inside:
            i[type] = val
        if not inside and find in name:
            inside = True
    return data
