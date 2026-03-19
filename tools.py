import json

def find_lamp(style):
    with open("lamps.json", "r", encoding="utf-8") as f:
        lamps = json.load(f)

    for lamp in lamps:
        if style.lower() in lamp["style"].lower():
            return lamp

    return lamps[0]