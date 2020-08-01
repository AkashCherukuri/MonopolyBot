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

def increment(init_pos, roll):
    return ((init_pos + roll) % 40)
