#!/usr/bin/python3

import sys
import pyfiglet

# ascii art called at specific points of the game
zelda = pyfiglet.figlet_format("ZELDA")
gameover = pyfiglet.figlet_format("GAME OVER")
keyart = pyfiglet.figlet_format("KEY")
doorart = pyfiglet.figlet_format("DOOR")

#change show Instructions to be more unique
def showInstructions():
    """Show the game instructions when called"""

#print a main menu and the commands
    print('''
    RPG Game
    ========
    Connected rooms on the map are shown by "-" or "|".
    Commands:
      Directions = "up, down, left, right"
      Keys = "yes, no"
      Unlock Door = "yes, no"
    ''')


# an inventory, which is initially empty
inventory = []

# At the start of the game, show the instructions for the user
showInstructions()

# create a class of Map and define the methods inside to call on when playing the game
class Map:

    def __init__(self, height, width, player_x, player_y, paths):
        self.height = height
        self.width = width
        self.x = player_x
        self.y = player_y
        self.paths = paths

    # making the moves for the player
    def move(self, direction):
        if direction == "up":
            if ((self.x, self.y -1), (self.x, self.y)) not in self.paths:
                print('Direction is blocked, choose a different route!')
            else:
                self.y -= 1
        if direction == "down":
            if ((self.x, self.y), (self.x, self.y + 1)) not in self.paths:
                print('Direction is blocked, choose a different route!')
            else:
                self.y += 1
        if direction == "right":
            if ((self.x, self.y), (self.x + 1, self.y)) not in self.paths:
                print('Direction is blocked, choose a different route!')
            else:
                self.x += 1
        if direction == "left":
            if ((self.x - 1, self.y), (self.x, self.y)) not in self.paths:
                print('Direction is blocked, choose a different route!')
            else:
                self.x -= 1

    # printing the map function
    def print_map(self):
            for y in range(0, self.height):

                # print the yth row of rooms
                for x in range(0, self.width):
                    if self.x == x and self.y == y:
                        sys.stdout.write("[x]")  # this is the player's room
                    else:
                        sys.stdout.write("[ ]")  # empty room
                    # now see whether there's a path to the next room
                    if ((x, y), (x + 1, y)) in self.paths:
                        sys.stdout.write("-")
                    elif ((x + 1, y), (x, y)) in self.paths:
                        sys.stdout.write("-")
                    else:
                        sys.stdout.write(" ")

                # now that we've written the rooms, draw paths to next row
                print()  # newline
                for x in range(0, self.width):
                    sys.stdout.write(" ")  # spaces for above room
                    if ((x, y), (x, y + 1)) in self.paths:
                        sys.stdout.write("|  ")
                    elif ((x, y + 1), (x, y)) in self.paths:
                        sys.stdout.write("|  ")
                    else:
                        sys.stdout.write("   ")
                print()

            # first room with a key in it, collect the key or not
            if (self.x, self.y) == keys[0]:
                print(keyart)
                grabKeys = input("\nThere is a key in this room! Do you want to grab it? (yes or no): ")
                if grabKeys == "yes":
                    print("You have collected a key!")
                    inventory.append("key")
                else:
                    print("You can come back and grab the key later.")

            # second room with a key, collect the key or not
            if (self.x, self.y) == keys[1]:
                print(keyart)
                grabKeys = input("\nThere is a key in this room! Do you want to grab it? (yes or no): ")
                if grabKeys == "yes":
                    print("You have collected a key!")
                    inventory.append("key")
                else:
                    print("You can come back and grab the key later.")

            # if you come across a locked door, there are two of them
            if ((self.x, self.y), (self.x, self.y + 1)) == lockedDoors[0]:
                print(doorart)
                unlockDoor = input("\nWould you like to open the locked door? You need a key to do so. (yes or no): ")
                if unlockDoor == "yes" and len(inventory) == 0:
                    print("You do not have a key to unlock the door! Please retrieve a key first!")
                    self.y += 1
                elif unlockDoor == "yes" and inventory[0]:
                    inventory.remove("key")
                    print("Door is unlocked! You may proceed!")
                elif unlockDoor == "no":
                    print("Door is still locked")
                    self.y += 1

            # second locked door
            if ((self.x, self.y), (self.x - 1, self.y)) == lockedDoors[1]:
                print(doorart)
                unlockDoor = input("\nWould you like to open the locked door? You need a key to do so. (yes or no): ")
                if unlockDoor == "yes" and len(inventory) == 0:
                    print("You do not have a key to unlock the door! Please retrieve a key first!")
                    self.x += 1
                elif unlockDoor == "yes" and inventory[0]:
                    inventory.remove("key")
                    print("Door is unlocked! You may proceed!")
                elif unlockDoor == "no":
                    print("Door is still locked")
                    self.x += 1

            # battling the boss (still working on it)
#            if (self.x, self.y) == boss[0]:
#                while True:
#                    characters = {
#                            "Gannon": {
#                                "HP" : 100,
#                                "Attack" : "Stomp"
#                                },
#                            "Link": {
#                                "HP" : 100,
#                                "Attack" : "Slash"
#                                }
#                            }
#                    print("You have entered the boss room to fight Gannon!")
#                    print(f"Gannon : {characters[0]}")
#                    print(f"Link : {characters[1]}")

            # getting to the last room that includes the triforce        
            if (self.x, self.y) == triforce[0]:
                print("You have found the epic Triforce!")
                inventory.append("triforce")

# defining rooms with keys
keys = [(4, 4), (2, 0)]

# defining the room with the triforce
triforce = [(0, 0)]

# defining the boss room
boss = [(1, 0)]

# defining all of the possible paths the player can take
paths = [((1, 4), (2, 4)),
         ((2, 4), (1, 4)),
         ((1, 4), (0, 4)),
         ((0, 4), (1, 4)),
         ((0, 4), (0, 3)),
         ((0, 3), (0, 4)),
         ((0, 3), (1, 3)),
         ((1, 3), (0, 3)),
         ((1, 3), (2, 3)),
         ((2, 3), (1, 3)),
         ((2, 3), (2, 2)),
         ((2, 2), (2, 3)),
         ((2, 3), (3, 3)),
         ((3, 3), (3, 4)),
         ((3, 4), (4, 4)),
         ((4, 4), (3, 4)),
         ((3, 4), (3, 3)),
         ((3, 3), (2, 3)),
         ((2, 2), (3, 2)),
         ((3, 2), (4, 2)),
         ((4, 2), (4, 1)),
         ((4, 1), (4, 2)),
         ((4, 1), (4, 0)),
         ((4, 0), (4, 1)),
         ((4, 0), (3, 0)),
         ((3, 0), (4, 0)),
         ((3, 0), (2, 0)),
         ((2, 0), (3, 0)),
         ((2, 0), (1, 0)),
         ((1, 0), (2, 0)),
         ((0, 0), (1, 0)),
         ((1, 0), (0, 0))]

# defining the two paths with the locked door
lockedDoors = [((2, 2), (2, 3)), ((1, 0), (0, 0))]

# defining the map size, start point, and loading paths to "m"
m = Map(5, 5, 2, 4, paths)

# keeping the game going during each turn
while True:
    
    if "triforce" not in inventory:
        print(zelda)
        m.print_map()
        print("Inventory: ", inventory)
        direction = input("What direction do you want to move? [up, down, left, right] ")
        m.move(direction)

    # game ends when the "triforce" is collected
    else:
        print(gameover)
        print("You have saved the princess and the kingdom of Hyrule by collecting the Triforce! You win!")
        break