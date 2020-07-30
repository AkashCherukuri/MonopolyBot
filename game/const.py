from enum import Enum

class State(Enum):
    GAME_LOBBY = 0 #Number of players not known yet
    GAME_BEGIN = 1 #Initialising Game, distribute money and stuff
    GAME_CONT = 2 #Game being played by humans/bots
    GAME_END = 3 #End the game if anyone person has been bankrupted or all humans decide to end game
        