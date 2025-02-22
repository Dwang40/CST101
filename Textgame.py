# Imports


# Instructions for the textGame
print("Welcome to my text based puzzle game about surviving the night by fortifying your house")
print("You play this game by inputting text in the console, use the help command to find out all the commands.")
print("This game is caps sensitive and every command is in the lower case.")
print("The house has living room, bathroom, kitchen, bedroom, attic, dining room and an backyard.")
print("Where would you like to go first?")

# Variables for the game
boolean = True
location = "livingRoom"
inventory = ["nothing"]

# Boolean to check if you have entered room before
enteredLivingRoom = False
enteredBathroom = False
enteredKitchen = False
enteredBedroom = False
enteredDiningRoom = False
enteredAttic = False 
enteredBackyard = False

# Arrays for the rooms
arrayLivingRoom = ["nCouch", "nFireplace", "nTrashCan", "nWindow"]

# functions for the game
def help(String):
    if(String == "help"):
        print("Command 1: scan <room>")
        print("This command scans the room for every object you can interact with in the room. You have to be in the room to search the room.")
        print("Command 2: search <object>")
        print("This command searches the object for the object in the room")

#text for the game
while boolean == True:
    if enteredLivingRoom == False and input() == "livingroom":
        print("You have entered the living room.")
        print("test text")
        print("What would you like to do?")
        enteredLivingRoom = True
    if enteredLivingRoom == True and input() == "livingroom":
        print("You have entered the living room.")
        print("What would you like to do?")
    help(input())
    if(input() == "end"):
        break
#idea make the entire thing a definition

    
    




