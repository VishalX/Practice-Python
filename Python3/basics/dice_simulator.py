"""
This small rollDice function simulates rolling of Dice.
A Dice has 6-faces, with values 1 to 6.None
"""

# Import Random module
import random

def rollDice():
    # Generate a number
    num = (random.randint(1, 100) % 6) + 1
    return num

if __name__=="__main__":
    val = int()
    while True:
        inp = input("Enter to Roll | Type 'x' to exit :")
        if inp == "x": break
        if len(inp) < 1:
            print(rollDice())
        else:
            print("[INPUT] Invalid input value")


