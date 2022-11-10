"""This python program uses pyfiglet and colorama  
    you can install colorama with the "pip install colorama" command in your linux terminal
    you can install pyfiglet withthe "pip install pyfiglet" command in your linux terminal"""

import random
import pyfiglet
import colorama
from colorama import Fore

banner = pyfiglet.figlet_format("A Game Of Rock, Paper, Scissors", font = "slant"  )
print(Fore.GREEN + banner) #Fore.Green changes my text to green

def main():


    # Game play options
    playOptions = ["Rock", "Paper", "Scissors", "Q"]



    #assign a random play to the computer
    computer = playOptions[random.randint(0,2)]

    #set gamePlay to False
    gamePlay = False

    while gamePlay == False:

    #set gamePlay to True
        gamePlay = input("Player, please choose a play: Rock, Paper, or Scissors? (or type X to exit)")

        if gamePlay == "X":
            exit()
        if gamePlay == computer:
            print("It's a Draw")
        elif gamePlay == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", gamePlay)
            else:
                print("You win!", gamePlay, "breaks", computer)
        elif gamePlay == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", gamePlay)
            else:
                print("You win!", gamePlay, "covers", computer)
        elif gamePlay == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "breaks", gamePlay)
            else:
                print("You win!", gamePlay, "cut", computer)
        else:
            print("That is an invalid game play word, check your spelling and make sure the first letter is Capitalized!")

    #set gamePlay to false again to loop the game
        gamePlay = False
        computer = playOptions[random.randint(0,2)]

main()
