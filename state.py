import json
from player import *
from tiles import tiles

class State:
    colors = ['#da00fe', '#fea600', "#fe4138", "#0072BB", "#29b30f", "#00e2e5"]  
    max_players = 2
    fake_rolls = [(3,4), (1,1)]
    cur_roll = -1 

    def get_roll(self):
        State.cur_roll += 1
        return State.fake_rolls[State.cur_roll]

    def process_roll(self):
        (a,b) = self.get_roll()
        self.players[self.cur_player()].location += a + b 
        self.players[self.cur_player()].location %= 40 

        # change to if tiles[location] == 'property'
        if (self.players[self.cur_player()].location == 7):
            self.currentSituation = 'buy_or_auction'

        if a != b:
            self.currentTurn += 1
            self.currentTurn %= len(self.playerIds)

    def __init__(self):
        self.tiles = tiles.tiles
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

        if len(self.playerIds) == State.max_players:
            self.currentSituation = 'waiting_for_dice_roll'

        State.colors.append(State.colors[0])
        del State.colors[0]

    def json(self):
        return {
            "tiles": self.tiles,
            "currentTurn": self.currentTurn,
            "players": self.players,
            "playerIds": self.playerIds,
            "currentSituation": self.currentSituation,
            "currentTile": self.currentTile,
            "auction": self.auction,
            "currentSpecialDescription": self.currentSpecialDescription
        }


