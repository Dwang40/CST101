# Imports 
import time
import math
import random

# 0: HP, 1: MAXHP, 2: ATK, 3: DEF, 4: SPD, 5: Lv, 6: EXP, 7: SP
character = [25, 25, 100, 2, 3, 1, 0, 0]

# Enemies 
# 0: HP, 1: ATK, 2: DEF, 3: SPD, 4: EXP, 5: DOT
gslime = [10, 3, 2, 1, 12, 2]
rslime = [10, 5, 1, 2, 15, 0]
goblin = [15, 3, 1, 1, 20, 0]
possessedTree = [60, 3, 6, 1, 1000, 0]

def stats():
    totalExp = character[5] * 10;
    print("Level:", character[5])
    print("EXP: ", character[6], "/", totalExp, sep = "")
    print("HP: ", character[0], "/", character[1],sep = "")
    print("ATK:", character[2])
    print("DEF:", character[3])
    print("SPD:", character[4])

def checkExp():
    while character[6] >= character[5] * 10:
        levelUp()
    
def restoreLife(int):
    if (character[0] + int < character[1]):
        character[0] += int
    else:
        character[0] = character[1]

def levelUp():
    character[5] += 1
    character[6] -= (character[5]-1) * 10
    character[3] += 1
    character[1] += 10
    character[2] += 1
    print("You have leveled up!")
    print("you have gained 10 HP, 1 ATK and 1 DEF")

def RNG(int):
    return random.randint(0, int)

#How much a player deals to an enemy
def playerDamage(player, enemy):
    damage = math.floor((player[2] * 1.5) - enemy[2])
    if(damage < 0):
        return 0;
    else:
        return damage

#How much a enemy deals to an player
def enemyDamage(enemy, player):
    damage = math.floor((enemy[1] * 1.5) - player[3])
    if(damage < 0):
        return 0;
    else:
        return damage

def speedCheck(player, enemy):
    if(player[4] == enemy[3]):
        if (RNG(2) == 1):
            return "player"
        else:
            return "enemy"
    if(player[4] > enemy[3]):
        return "player"
    else:
        return "enemy"

# probably returns a int array with damage that turn
def battle(player, enemy, stringE):
    damageEnemy = playerDamage(character, gslime)
    damagePlayer = enemyDamage(gslime, character)
    

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
        #if(RNG(2) == 1):
            gslime_encounter()
        #else: 
            #rslime_encounter()
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
    print("\nYou walk down the forest path, and come across a green blob.")
    time.sleep(1)
    while True:
        pHP = character[0]
        sHP = gslime[0]
        dmg = 0
        damageSlime = battle(character, gslime, "green slime")[0]
        damagePlayer = battle(character, gslime, "green slime")[1]
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
    
def rslime_encounter():
    damageSlime = playerDamage(character, rslime)
    damagePlayer = enemyDamage(rslime, character)
    print(damagePlayer)
    pHP = character[0]
    sHP = rslime[0]
    dmg = 0
    print("\nYou walk down the forest path, and come across a red blob.")
    time.sleep(1)
    while True:
        print("You attack the red slime and deals", damageSlime, "damage!")
        time.sleep(1)
        print("The red slime attacks you and deals", damagePlayer, "damage!")
        sHP -= damageSlime
        if (sHP <= 0):
            print("You won and gained", rslime[4],"EXP!")
            character[0] -= dmg
            character[6] += rslime[4]
            checkExp()
            crossroadsF()
        pHP -= damagePlayer 
        dmg += damagePlayer
        if(pHP <= 0):
            print("You lost! Better luck next time!")
            exit()
    
def treeEncounter():
    time.sleep(1)
    print("\nWalking for a bit longer, something sinister seems to be looking at you.")
    print("A giant tree blocks the way!")
    time.sleep(1)
    damageTree = playerDamage(character, possessedTree)
    damagePlayer = enemyDamage(possessedTree, character)
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
            checkExp()
            crossroadsF()
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
        restoreLife(9)
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
time.sleep(1)
print("Currently the only commands I have is \"stats\" which shows you your stats and the command \"end\" which ends the game.")
time.sleep(1)
start_game()
