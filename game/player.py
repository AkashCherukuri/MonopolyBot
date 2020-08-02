class Player:
    def __init__(self):
        self.pos = 0
        self.money = 0
        self.alias = None
        self.owned_prop = [] #We add in the ids of owned cards

    def init(self, _alias):
        self.money = 1520 #Can be changed, but this is per the official rules.
        self.alias = _alias
    
    #Used to set the position of player on board.
    def set_pos(self, pos):
        self.pos = pos

    def ret_pos(self):
        return self.pos

    #Pay rents, mon will be -ve to add money to player.
    def pay(self, mon):
        self.money = self.money - mon
        return (self.money)