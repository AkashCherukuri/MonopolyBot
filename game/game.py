from itertools import cycle
from .board import Board
from .utils import *
from .const import State
from .player import Player

class Game:
    def __init__(self):
        self.state = None
        self.bank_houses = 32
        self.bank_hotels = 12
        self.players = []
        self.turn_cycler = None
        self.turn = None

    def init(self):
        self.board = Board()
        self.board.init()
        self.state = State.GAME_BEGIN
        print(f"Game of Monopoly has been initialized. Please follow the instructions on screen and enter your inputs accordingly.\n")
    
    def add_player(self):
        new = Player()
        new.init(prompt(f"Enter alias for Player{len(self.players) + 1}"))
        self.players.append(new)

    def is_prop(self, card):
        colors = ["Brown", "Blue", "Pink", "Orange", "Red", "Yellow", "Green", "DBlue"]
        if card["color"] in colors:
            return True
        else:
            return False

    def check_owner(self, id):
        check = None
        for player in self.players:
            if id in player.owned_prop:
                check = player
        return check

    def advance_turn(self):
        self.turn = next(self.turn_cycler)
    
    #Bonus awarded to players for passing through GO
    def GO_Bonus(self, player):
        player.pay(-200)
        return True

    #Check number of Houses and Hotels and return rent
    def find_rent(self, card):
        num_houses = card["num_hs"]
        num_hotels = card["num_ht"]

        if num_hotels != 0:
            return (card["htr"])
        elif num_houses == 0:
            return (card["rent"])
        else:
            tag = "h" + str(num_houses) + "r"
            return (card[tag])
    
    #Returns True if property has been developed; and returns False if not possible to do so
    #TODO: Make the fn check if all colors have been fully developed before developing hotels
    def dev_prop(self, card, player):
        if card.card["num_ht"] == 1:
            return False
        elif self.bank_houses != 0 and card.card["num_hs"] < 4:
            card.card["num_hs"] += 1
            self.bank_houses = self.bank_houses - 1
            player.pay(card.card["hsc"])
            return True
        elif self.bank_hotels != 0 and card.card["num_hs"] == 4:
            card.card["num_hs"] = 0
            self.bank_houses += 4
            self.bank_hotels = self.bank_hotels - 1
            card.card["num_ht"] = 1
            player.pay(card.card["hsc"])
            return True
        else:
            return False

    def find_card(self, id, board):
        for card in board.board:
            if card.card["id"] == id:
                return card

    #Current turn player pays rent to player in argument
    def pay_rent(self, player, rent):
        player.pay(-1 * rent)
        self.turn.pay(rent)

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

            self.state = State.TURN_BEGIN
            self.evaluate()
        
        elif self.state == State.TURN_BEGIN:
            print(f"--- {self.turn.alias}'s Turn --- \n")
            _roll = roll()
            #Need to add check for double rolls
            print(f"{self.turn.alias} rolled a {_roll}! Advancing the player through {_roll} blocks...")
            
            (new_pos, bonus) = increment(self.turn.ret_pos(), _roll)
            if bonus:
                print(f"Adding 200$ for passing through GO...")
                self.GO_Bonus(self.turn)
            
            self.turn.set_pos(new_pos)
            card = self.board.board[new_pos].card
            id = card["id"]

            #TODO: Maybe add a info() in player.py to print out details of the card...
            print(f"{self.turn.alias}, you've reached {id}!\n")

            #If not owned, prompt to buy property IF IT IS A PROPERTY
            if self.check_owner(id) is None and self.is_prop(card):
                cost = card["cost"]
                resp = prompt(f"{id} is NOT owned by anyone yet. The cost to buy this property is {cost}. Do you want to but this property? (Y/N)")
                if resp == 'y' or resp == 'Y':
                    self.turn.pay(cost)
                    self.turn.owned_prop.append(id)
                    print(f"{self.turn.alias} has bought {id} for {cost}. Remaining money is {self.turn.money}.")
                #TODO: Make auctioning possible here
                elif resp == 'n' or resp == 'N':
                    print(f"Property not bought.")
                else:
                    print(f"Unknown response... Interpreting as disinterest in buying property.")

            elif self.check_owner(id) is not None and self.is_prop(card):
                rent = self.find_rent(card)
                print(f"This property is owned by {self.check_owner(id).alias}. Paying a rent of {rent} to the owner...")
                self.pay_rent(self.check_owner(id), rent)
                print(f"Remaining money is {self.turn.money}.")

            elif card["color"] == "CC" or card["color"] == "C":
                #TODO: Add Functionality for Chance, Community Chests
                div = True
                if card["color"] == "CC":
                    div = False
                print(f"Drawing a card from the pile...")
                print(f"{self.turn.alias} has drawn a card, and it says... {self.board.draw(div)}")
                prompt(f"Do you agree?")
            print()

            self.state = State.TURN_END
            self.evaluate()

        elif self.state == State.TURN_END:
            #TODO: Has the global prompt to buy houses anywhere or smth
            #TODO: info() which prints the number of houses and hotels in the bank's stock
            print(f"{self.turn.alias}'s turn has ended. The bank has {self.bank_houses} houses in stock, and {self.bank_hotels} hotels in stock.")
            while True:
                entry = prompt(f"Anyone willing to buy houses or hotels for properties, enter your alias below. Enter 'X' if no one is interested:")

                check = False

                if entry == 'x' or check == 'X':
                    print(f"Ending Bidding Stage...")
                    break
            
                for player in self.players:
                    if player.alias == entry:
                        check = True
                        if len(player.owned_prop) != 0:
                            print(f"{player.alias}, you own the following properties:")
                            i = 1
                            for prop in player.owned_prop:
                                print(f"{prop} ({i})")
                                i+=1
                            #TODO: Failsafe here if input is not integer
                            inp = int(prompt(f"Please enter the id of the property you'd like to develop:"))
                            prop_id = player.owned_prop[inp-1]
                            prop_card = self.find_card(prop_id, self.board)
                            if self.dev_prop(prop_card, player):
                                hs = prop_card.card["num_hs"]
                                ht = prop_card.card["num_ht"]
                                print(f"Property developed. This property now has {hs} houses, and {ht} hotels.")
                            else:
                                print(f"Property not Developed.")
                        else:
                            print(f"{player.alias}, you own no properties, meaning you can't buy any houses.")

                if not check:
                    print(f"Alias not found, please try again.")


            #TODO: Check for double throw, and repeat turn if that is the case
            self.advance_turn()
            self.state = State.TURN_BEGIN
            self.evaluate()
