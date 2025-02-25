import time
import math

# HP, MAXHP, ATK, DEF, SPD, Lv, EXP
character = [25, 25, 4, 2, 3, 1, 0]

# Enemies 
# HP, ATK, DEF, SPD, EXP, DOT
gslime = [10, 2, 2, 1, 12, 2]
rslime = [7, 4, 2, 2, 15, 0]
goblin = [15, 3, 1, 1, 20, 0]
possessedTree = [60, 3, 6, 1, 10, 0]

def stats():
    totalExp = character[5] * 10;
    print("Level:", character[5])
    print("EXP: ", character[6], "/", totalExp, sep = "")
    print("HP: ", character[0], "/", character[1],sep = "")
    print("ATK:", character[2])
    print("DEF:", character[3])
    print("SPD:", character[4])

def checkExp(array):
    if array[6] >= array[5] * 10:
        return True
    else:
        return False

def restoreLife(int):
    if (character[0] + int < character[1]):
        character[0] += int
    else:
        character[0] = character[1]

def levelUp(array):
    array[5] += 1
    array[6] -= (array[5]-1) * 10
    array[3] += 1
    array[1] += 10
    array[2] += 1
    print("You have leveled up!")
    print("you have gained 10 HP, 1 ATK and 1 DEF")

def damageCalculation(array, array2):
    damage = math.floor((array[2] * 1.5) - array2[3])
    if(damage < 0):
        return 0;
    else:
        return damage

def battle(array, array2):
    print(0)

def start_game():
    print("Welcome to the Beginner's Forest!")
    time.sleep(1)
    print("You find yourself at the entrance of an forest. This is where all heroes begin their adventure.")
    time.sleep(1)
    choice1 = input("Do you enter the forest? (yes/no): ")
    
    if choice1 == "yes":
        enter_forest()
    else:
        print("You decide not to start your adventure. Maybe another time!")
        exit()

def enter_forest():
    print("\nYou step into the forest, and the trees seem to whisper around you.")
    time.sleep(1)
    print("After walking for a while, you see 3 seperate paths.")
    time.sleep(1)
    crossroadsF()

def crossroadsF():
    choice2 = input("Do you go left or right? (left/middle/right): ").strip().lower()
    if choice2 == "left":
        gslime_encounter()
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

def gslime_encounter():
    damageSlime = damageCalculation(character, gslime)
    damagePlayer = damageCalculation(gslime, character)
    pHP = character[0]
    sHP = gslime[0]
    dmg = 0
    print("\nYou walk down the forest path, and come across a green blob.")
    time.sleep(1)
    while True:
        print("You attack the green slime and deals", damageSlime, "damage!")
        time.sleep(1)
        print("The green slime attacks you and deals", damagePlayer, "damage!")
        time.sleep(1)
        print("The green slime inflicts 2 points of posion damage!")
        sHP -= damageSlime
        if (sHP <= 0):
            print("You won and gained", gslime[4],"EXP!")
            character[0] -= dmg
            character[6] += gslime[4]
            if(checkExp(character) == True):
                levelUp(character)
            crossroadsF()
        pHP -= damagePlayer 
        dmg += damagePlayer + 2
        if(pHP <= 0):
            print("You lost! Better luck next time!")
            exit()
    
def treeEncounter():
    time.sleep(1)
    print("\nWalking for a bit longer, something sinister seems to be looking at you.")
    print("A giant tree blocks the way!")
    time.sleep(1)
    damageTree = damageCalculation(character, possessedTree)
    damagePlayer = damageCalculation(possessedTree, character)
    pHP = character[0]
    sHP = possessedTree[0]
    dmg = 0
    while True:
        print("You attack the giant tree and deals", damageTree, "damage!")
        time.sleep(1)
        print("The giant tree attacks you and deals", damagePlayer, "damage!")
        sHP -= damageTree
        if (sHP <= 0):
            time.sleep(1)
            print("You won and gained", possessedTree[4],"EXP!")
            character[0] -= dmg
            character[6] += possessedTree[4]
            if(checkExp(character) == True):
                levelUp(character)
            exit()
        pHP -= damagePlayer 
        dmg += damagePlayer
        if(pHP <= 0):
            time.sleep(1)
            print("You lost! Better luck next time!")
            time.sleep(1)
            print("Thanks for playing my short demo!")
            exit()

def campfire():
        print("\nWalking deeper into the forest, you come across a safe spot.")
        time.sleep(1)
        print("There seems to be no monsters around and a small campfire is visible.")
        time.sleep(1)
        campfire2()

def campfire2():
    choice = input("You decide to rest here. (rest/use points): ")
    if (choice == "rest"):
        time.sleep(1)
        print("Sleeping near the campfire has restored 20 HP")
        restoreLife(100)
        crossroadsF()
    if (choice == "use points"):
        print("You have decided to use your skill points.") 
        time.sleep(1)
        print("What stat would you like to increase?")
        time.sleep(1)
        choice2 = input("(HP/ATK/DEF/SPD): ")
        if(choice2 == "HP"):
            print("You have gained 10 HP.")
            character[1] += 10
            crossroadsF()
        if(choice2 == "ATK"):
            print("You have gained 1 ATK.")
            character[2] += 1
            crossroadsF()
        if(choice2 == "DEF"):
            print("You have gained 1 DEF.")
            character[3] += 1
            crossroadsF()
        if(choice2 == "SPD"):
            print("You have gained 1 SPD.")
            character[4] += 1
            crossroadsF()
    if(choice == "stats"):
        time.sleep(1)
        stats()
        campfire2()
    if(choice == "end"):
        exit()
    
# Start the game
print("Currently the only commands I have is \"stats\" which shows you your stats and the command \"end\" which ends the game.")
start_game()
