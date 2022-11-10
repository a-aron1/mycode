from random import randint
import pyfiglet
import colorama
from colorama import Fore

banner = pyfiglet.figlet_format("A Game Of Rock, Paper, Scissors", font = "slant"  )
print(Fore.GREEN + banner) #Fore.Green changes my text to green

# Game play options
playOptions = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = playOptions[randint(0,2)]

#set gamePlay to False
gamePlay = False

while gamePlay == False:

#set gamePlay to True
    gamePlay = input("Player, please choose a play: Rock, Paper, or Scissors?")
    if gamePlay == computer:
        print(pyfiglet.figlet_format("Tie!"))
    elif gamePlay == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", gamePlay)
        else:
            print("You win!", gamePlay, "smashes", computer)
    elif gamePlay == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", gamePlay)
        else:
            print("You win!", gamePlay, "covers", computer)
    elif gamePlay == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", gamePlay)
        else:
            print("You win!", gamePlay, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    #set gamePlay to false again to loop the game
    gamePlay = False
    computer = playOptions[randint(0,2)]