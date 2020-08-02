from enum import Enum

class State(Enum):
    GAME_BEGIN = 1 #Initialising Game, distribute money and stuff
    TURN_BEGIN = 2 #Turn of a player/bot begins
    TURN_END = 3 #End a player's turn, and ask everyone if they wanna build houses somewhere
    GAME_END = 4 #End the game if anyone person has been bankrupted or all humans decide to end game
        