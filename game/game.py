from itertools import cycle
from board import Board
from utils import *
from const import State
from player import Player

class Game:
    def __init__(self):
        self.state = None
        self.players = []
        self.turn_cycler = None
        self.turn = None

    def init(self):
        self.board = Board()
        self.board.init()
        self.state = State.GAME_LOBBY
        print(f"Game of Monopoly has been initialized. Please follow the instructions on screen and enter your inputs accordingly.\n")
    
    def add_player(self):
        new = Player()
        new.init(prompt(f"Enter alias for Player{len(self.players) + 1}"))
        self.players.append(new)

    def advance_turn(self):
        self.turn = next(self.turn_cycler)
    
    #All game logic in here
    def evaluate(self):
        if self.state == State.GAME_LOBBY:
            while True:
                num_players = int(prompt(f"Please enter the number of players."))
                if num_players < 9 and num_players > 1:
                    for i in range(num_players):
                        self.add_player()
                    break
                else:
                    print(f"Only 2 to 8 players are supported as of now, please try again.\n")

            self.turn_cycler = cycle(self.players)
            self.advance_turn()

            self.state = State.GAME_BEGIN
            self.evaluate()
        
        elif self.state == State.GAME_BEGIN:
            pass
