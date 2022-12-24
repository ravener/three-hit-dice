import os
import time
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def validate(guess):
    if len(guess) == 3 and all(map(lambda i: i in ["U", "D"], guess)):
        return guess
    
    print("Invalid Input.")
    exit(1)

clear()
p1 = list(validate(input("Player 1's Guess: ").upper()))
clear()
p2 = list(validate(input("Player 2's Guess: ").upper()))
clear()
input("Press Enter to Start the Game!")
clear()

rolls = []
nums = []

while True:
    clear()

    dice = random.randint(1, 6)
    nums.append(str(dice))
    rolls.append("U" if dice > 3 else "D")

    print(" ".join(nums))
    print(" ".join(rolls))
    
    if len(rolls) >= 3:
        if rolls[-3:] == p1 or rolls[-3:] == p2:
            if p1 == p2:
                print("{} was rolled and it was a draw!".format("".join(rolls[-3:])))
                break
        if rolls[-3:] == p1:
            print("Player 1 Wins with {}!".format("".join(p1)))
            print("Player 2's guess was {}".format("".join(p2)))
            break
        if rolls[-3:] == p2:
            print("Player 2 Wins with {}!".format("".join(p2)))
            print("Player 1's guess was {}".format("".join(p1)))
            break

    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.6)

    print()
