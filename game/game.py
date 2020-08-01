from itertools import cycle
from board import Board
from utils import *
from const import State
from player import Player

class Game:
    def __init__(self):
        self.state = None
        self.num_houses = 32
        self.num_hotels = 12
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
    
    #Bonus awarded to players for passing through GO
    def GO_Bonus(self, player):
        player.pay(-200)
        return True

    #All game logic in here.
    def evaluate(self):
        if self.state == State.GAME_BEGIN:
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

            self.state = State.GAME_CONT
            self.evaluate()
        
        elif self.state == State.GAME_CONT:
            print(f"--- {self.turn.alias}'s Turn --- \n")
            _roll = roll()
            #Need to add check for double rolls
            print(f"{self.turn.alias} rolled a {_roll}! Advancing the player through {_roll} blocks...")
            
            (new_pos, bonus) = increment(self.turn.ret_pos(), _roll)
            if bonus:
                print(f"Adding 200$ for passing through GO...")
                self.GO_Bonus(self.turn)
            
            self.turn.set_pos(new_pos)
            id = self.board.board[new_pos].card["id"]
            print(f"{self.turn.alias}, you've reached {id}!\n")

            self.advance_turn()
            self.evaluate()
