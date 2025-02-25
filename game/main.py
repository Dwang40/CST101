# Imports 
import time
import math
import random
import battle
import check
import encounter
import command

# 0: HP, 1: MAXHP, 2: ATK, 3: DEF, 4: SPD, 5: Lv, 6: EXP, 7: SP
character = [25, 25, 100, 2, 3, 1, 0, 0]

# Enemies 
# 0: HP, 1: ATK, 2: DEF, 3: SPD, 4: EXP, 5: DOT
gslime = [10, 3, 2, 1, 12, 2]
rslime = [10, 5, 1, 2, 15, 0]
goblin = [15, 3, 1, 1, 20, 0]
possessedTree = [60, 3, 6, 1, 1000, 0]

def start():
    print("Welcome to the Beginner's Forest!")
    time.sleep(1)
    print("You find yourself at the entrance of an forest. This is where all heroes begin their adventure.")
    time.sleep(1)
    choice = input("Do you enter the forest? (yes/no): ")
    
    if choice == "yes":
        enterForest()
    else:
        print("You decide not to start your adventure. Maybe another time!")
        exit()


def crossroadsF1():
    choice2 = input("Do you go left or right? (left/middle/right): ").strip().lower()
    if choice2 == "left":
        encounter.gslime()
    if choice2 == "middle":
        campfire()
    elif choice2 == "right":
        treeEncounter()
    elif choice2 == "end":
        exit()
        crossroadsF()
    elif choice2 == "stats":
        stats()
        crossroadsF()
    else:
        print("This is an invaild option. Try again.")
        crossroadsF()