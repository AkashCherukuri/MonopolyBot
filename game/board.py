from .info import id, color, cost, rent, hsc, h1r, h2r, h3r, h4r, htr, ChC_Desc, ComC_Desc
import random

#Total 40 cards are present on the board.
class Card:
    def __init__(self):
        self.card = {"id": None, "color": None, "cost": None, "rent": None, "hsc": None, "h1r": None, "h2r": None, "h3r": None, "h4r": None, "htr": None, "num_hs": 0, "num_ht": 0}


class Board:
    def __init__(self):
        self.board = []

    def init(self):
        for _id in id:
            _card = Card()
            _card.card["id"] = _id
            self.board.append(_card)

        for i in range(len(id)):
            self.board[i].card["color"] = color[i]
            self.board[i].card["cost"] = cost[i]
            self.board[i].card["rent"] = rent[i]
            self.board[i].card["hsc"] = hsc[i]
            self.board[i].card["h1r"] = h1r[i]
            self.board[i].card["h2r"] = h2r[i]
            self.board[i].card["h3r"] = h3r[i]
            self.board[i].card["h4r"] = h4r[i]
            self.board[i].card["htr"] = htr[i]

        self.ch_cards = ChC_Desc
        self.com_cards = ComC_Desc

        random.shuffle(self.ch_cards)
        random.shuffle(self.com_cards)

    #div is a bool; if True then chance is drawn, if False then Community chest is drawn; and drawn card is shifted to bottom of deck
    def draw(self, div):
        if div:
            deck = self.ch_cards
        else:
            deck = self.com_cards
        deck.append(deck[0])
        deck.pop(0)
        return deck[-1]
