import json

class Player:
    def __init__(self, name, color, money=200, cards=0, location=0):
        self.username = name;
        self.color = color
        self.money = money
        self.cards = cards
        self.location = location

    def json(self):
        return {
            "money" : self.money,
            "cards" : self.color,
            "location" : self.location,
            "username" : self.username,
            "color" : self.color
        }


