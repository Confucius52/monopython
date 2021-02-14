import json
from player import * 

class State:
    colors = ['#da00fe', '#fea600', "#fe4138", "#0072BB", "#29b30f", "#00e2e5"]  
    fake_rolls = [(3,4), (1,1)]
    cur_roll = -1 
    
    def get_roll():
        State.cur_roll += 1

        return State.fake_rolls[cur_roll]

    def process_roll():
        (a,b) = get_roll()
        
    
    def __init__(self):
        self.tiles = []
        self.currentTurn = 0
        self.players = dict()
        self.playerIds = []
        self.currentSituation = 'lobby'
        self.currentTile = 0
        self.auction = None
        self.currentSpecialDescription = ''

    def cur_player(self):
        return self.playerIds[self.currentTurn]
    
    def add_player(self, data):
        self.players[data['id']] = Player(data['username'], State.colors[0])
        self.playerIds.append(data['id'])

        State.colors.append(State.colors[0])
        del State.colors[0]

    def json(self):
        return {
            "tiles" : self.tiles,
            "currentTurn" : self.currentTurn,
            "players" : self.players,
            "playerIds" : self.playerIds,
            "currentSituation" : self.currentSituation,
            "currentTile" : self.currentTile,
            "auction" : self.auction,
            "currentSpecialDescription" : self.currentSpecialDescription
        }
