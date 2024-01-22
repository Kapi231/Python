
import random

playerInput = int(input("\n1 - Rock\n2 - Paper\n3 - Scisors\n\nChoose your tool: "))

num = random.randint(0, 2)

def looseFunction():
    print("\nYOU LOST!")
    exit()

def winFunction():
    print("\nYOU WON!")
    exit()

if num == 0:
    print("\nROCK!")
    if playerInput != 2:
        looseFunction()
    else:
        winFunction()

elif num == 1:
    print("\nPAPER!")
    if playerInput != 3:
        looseFunction()
    else:
        winFunction()

elif num == 2:
    print("\nSCISORS")
    if playerInput != 1:
        looseFunction()
    else:
        winFunction()
