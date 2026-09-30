import json

DATA_FILE = "fleet.json"


def load_fleet(filename=DATA_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:

        return {}

def save_fleet(fleet, filename = DATA_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(fleet, file, ensure_ascii=False, indent=4)