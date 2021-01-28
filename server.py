import json

state = {"players": []}


def process_data(data):
    if data['action'] == "join":
        player = {"username": data['username'], "money": 200}
        state['players'].append(player)

process_data({"action": "join", "username": "greenpizza12"})

print(json.dumps(state))
