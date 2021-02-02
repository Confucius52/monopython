import json
from random import randint

state = {"players": dict(), "currentTurn": 0, "playerIds": [], "currentSituation": 'lobby'}

def cur_player():
    return state["playerIds"][state["currentTurn"]]

colors = ['#da00fe', '#fea600', "#fe4138", "#0072BB", "#29b30f", "#00e2e5"]  

fake_rolls = [(3,4), (1,1)]
cur_roll = -1 
def get_roll():
    global cur_roll
    cur_roll += 1

    return fake_rolls[cur_roll]

def process_roll():
    (a,b) = get_roll()

    state["players"][cur_player()]["location"] += a + b
    state["players"][cur_player()]["location"] %= 40
     
    if a != b:
        state["currentTurn"] += 1 
        state["currentTurn"] %= len(state["players"]) 

def process_data(data): 
    action = data['action']

    if action == "join":
        player = {"username": data['username'], "money": 200, "location": 0, "cards": 0, "color": colors[0]}
        state["playerIds"].append(data['id'])
        state["players"][data['id']] = player
        
        colors.append(colors[0])
        del colors[:1]
    elif action == 'roll_dice':
        process_roll() 

    elif action == 'leave':
        pass

def send_data(data):
    pass

