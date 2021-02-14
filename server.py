import json
from player import *
from state import *
from random import randint

# cur_state.state = {"players": dict(), "currentTurn": 0, "playerIds": [], "currentSituation": 'lobby'}
cur_state = State()

colors = ['#da00fe', '#fea600', "#fe4138", "#0072BB", "#29b30f", "#00e2e5"]  

fake_rolls = [(3,4), (1,1)]
cur_roll = -1 
def get_roll():
    global cur_roll
    cur_roll += 1

    return fake_rolls[cur_roll]

def process_roll():
    (a,b) = get_roll()

    # cur_state.state["players"][get_cur_player()].location += a + b
    # cur_state.state["players"][get_cur_player()]["location"] %= 40
     
    # if a != b:
    #     cur_state.state["currentTurn"] += 1 
    #     cur_state.state["currentTurn"] %= len(cur_state.state["players"]) 

def process_data(data): 
    action = data['action']

    if action == "join":
        cur_state.add_player(data) 
    elif action == 'roll_dice':
        cur_state.process_roll() 

    elif action == 'leave':
        pass

def send_data(data):
    pass

