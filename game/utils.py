from random import randint

def roll():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return (die1 + die2)
