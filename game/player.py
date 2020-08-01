class Player:
    def __init__(self):
        self.pos = 0
        self.money = 0
        self.alias = None
        self.owned_prop = []

    def init(self, _alias):
        self.money = 1520
        self.alias = _alias
