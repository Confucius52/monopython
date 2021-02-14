class Street:
    def __init__(self, position, color, full_name, split_name, cost, rent,
                 type, ownerId, level, house_cost, isMortgaged):
        self.position = position
        self.color = color
        self.full_name = full_name
        self.split_name = split_name
        self.cost = cost
        self.rent = rent
        self.type = type
        self.ownerId = ownerId
        self.level = level
        self.house_cost = house_cost
        self.isMortgaged = isMortgaged

    def json(self):
        return {
            "position": self.position,
            "color": self.color,
            "full_name": self.full_name,
            "split_name": self.split_name,
            "cost": self.cost,
            "rent": self.rent,
            "type": self.type,
            "ownerId": self.ownerId,
            "level": self.level,
            "house_cost": self.house_cost,
            "isMortgaged": self.isMortgaged,
        }
