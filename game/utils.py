from random import randint

def roll():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return (die1 + die2)

def prompt(str = ""):
    print(str)
    inp = input("Monpoly>> ")
    print()
    return inp

#bool refers to whether we've passed through GO, to award money to player
def increment(init_pos, roll):
    new = init_pos + roll
    if new > 39:
        return ((new - 40), True)
    else:
        return (new, False)