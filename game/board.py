import info

class Card:
    def __init__(self):
        self.card = {"id": None, "color": None, "cost": None, "rent": None, "hsc": None, "h1r": None, "h2r": None, "h3r": None, "h4r": None, "htr": None}

class Board:
    def __init__(self):
        self.board = []

    def init(self):
        for _id in info.id:
            _card = Card()
            _card.card["id"] = _id
            self.board.append(_card)

        for i in range(len(info.id)):
            self.board[i].card["color"] = info.color[i]
            self.board[i].card["cost"] = info.cost[i]
            self.board[i].card["rent"] = info.rent[i]
            self.board[i].card["hsc"] = info.hsc[i]
            self.board[i].card["h1r"] = info.h1r[i]
            self.board[i].card["h2r"] = info.h2r[i]
            self.board[i].card["h3r"] = info.h3r[i]
            self.board[i].card["h4r"] = info.h4r[i]
            self.board[i].card["htr"] = info.htr[i]
