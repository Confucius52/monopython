import json
from server import *
from pprint import pprint

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "json"):
            return obj.json()
        return json.JSONEncoder.default(self, obj)

actions = [
    {"action": "join", "username": "greenpizza12", "id": "0"},
    {"action": "join", "username": "elephant", "id": "1"},
    {"action": "roll_dice", "id": "1"},
]

def main():
    for action in actions:
        process_data(action)

    print(json.dumps(cur_state, indent = 2, cls = ComplexEncoder))


if __name__ == '__main__':
    main()
