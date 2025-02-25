# Imports 
import time
import math
import random
import battle
import check
import encounter
import main

# Character
# 0: HP, 1: MAXHP, 2: ATK, 3: DEF, 4: SPD, 5: Lv, 6: EXP, 7: SP
# Enemies 
# 0: HP, 1: ATK, 2: DEF, 3: SPD, 4: EXP, 5: DOT

def stats(character):
    totalExp = character[5] * 10;
    print("Level:", character[5])
    print("EXP: ", character[6], "/", totalExp, sep = "")
    print("HP: ", character[0], "/", character[1],sep = "")
    print("ATK:", character[2])
    print("DEF:", character[3])
    print("SPD:", character[4])
