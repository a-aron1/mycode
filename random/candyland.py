#!/usr/bin/python3

#PLEASE READ! You must do the following in the command line before running script:
# pip install pyfiglet

import pyfiglet

candyland = pyfiglet.figlet_format("CANDYLAND")
gameover = pyfiglet.figlet_format("GAME OVER")

print(candyland)

begin = input("Will this be a 1 player or 2 player game?\n>")
while begin == '1' or '2':
    if begin == '1':
        enterplayer1 = input("Enter your player (Bob, Alice, Pedro, Laura, Sam):\n>")
        enterplayer1 = enterplayer1.capitalize()
        break
    if begin == '2':
        enterplayer1 = input("Enter your player (Bob, Alice, Pedro, Laura, Sam):\n>")
        enterplayer2 = input("Enter your player (Jim, Chuck, Kira, Ell, Bre):\n>")
        enterplayer1 = enterplayer1.capitalize()
        enterplayer2 = enterplayer2.capitalize()
        break
    else:
        begin

spot = 0
spotb = 0
round = 0

answer1 = " "
answer2 = " "
answer3 = " "
answer4 = " "
answer5 = " "
answer1b = " "
answer2b = " "
answer3b = " "
answer4b = " "
answer5b = " "

#One Player Game
if begin == '1':
    while round < 1 and (answer1 != 'Gumdrops'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer1 = input('What are the squishy gelatin candies with sugar on the outside?\n>')
        answer1 = answer1.capitalize()
    if answer1 == 'Gumdrops':
        spot += 6
        print("Correct! You move ahead 6 steps!")
    else :
        print("Sorry " + enterplayer1 + ", the answer was Gumdrop. You don't get to move ahead any spaces.")
    print("Current spot: " + str(spot))

    while round < 2 and (answer2 != 'Butterfinger'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer2 = input('Keep your hands off of my ____________! (Nestle Brand)\n>')
        answer2 = answer2.capitalize()
    if answer2 =='Butterfinger':
        spot += 12
        print("Correct! You move ahead 12 steps!")
    else :
        print("Sorry, the answer was Butterfinger. You move back 6 spaces to the beginning.")
        spot = 0
    print("Current spot: " + str(spot))

    while round < 3 and (answer3 != 'Twix'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer3 = input("____ , Two for me, none for you!\n>")
        answer3 = answer3.capitalize()
    if answer3 == 'Twix':
        spot += 4
        print("Correct! You move ahead 4 steps!")
    elif (spot < 5):
        print("Sorry, the answer was Twix. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry, the answer was Twix. You move back 4 spaces.")
        spot -= 4
    print("Current spot: " + str(spot))

    while round < 4 and (answer4 != 'Skittles'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer4 = input("________ , taste the rainbow!\n>")
        answer4 = answer4.capitalize()
    if answer4 == 'Skittles':
        spot += 8
        print("Correct! You move ahead 8 steps!")
    elif (spot < 9):
        print("Sorry, the answer was Skittles. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry, the answer was Skittles. You move back 8 spaces.")
        spot -= 8
    print("Current spot: " + str(spot))

    while round < 5 and (answer5 != 'York'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer5 = input("Round pepperment pattie with dark chocolate on the outside. Shiny silver Packaging.\n>")
        answer5 = answer5.capitalize()
    if answer5 == 'York':
        spot += 4
        print("Correct! You move ahead 4 steps!")
    elif (spot < 5):
        print("Sorry, the answer was York. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry, the answer was Twix. You move back 4 spaces.")
        spot -= 4
    print("Current spot: " + str(spot))

    if (spot > 25):
        print("You have saved the land of candy from all of the children who conspire to erode the contents of this magical kingdom. Congratulations!")
        print(f"Final Score: {enterplayer1} : {spot}")
    if (spot < 25):
        print("You have failed to reach the point of saving the Candy Kingdom. Better luck next time!")
        print(f"Final Score: {enterplayer1} : {spot}")
        print(gameover)

#Two Player Game
if begin == '2':
    while round < 1 and (answer1 != 'Gumdrops'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer1 = input('What are the squishy gelatin candies with sugar on the outside?\n>')
        answer1 = answer1.capitalize()
        print(f"Round: {round} for {enterplayer2}")
        answer1b = input('What are the squishy gelatin candies with sugar on the outside?\n>')
        answer1b = answer1b.capitalize()
    if answer1 == 'Gumdrops':
        spot += 6
        print("Correct!" + enterplayer1 + " You move ahead 6 steps!")
    else :
        print("Sorry " + enterplayer1 + ", the answer was Gumdrop. You don't get to move ahead any spaces.")
    print("Current spot: " + enterplayer1 + " : "+ str(spot))
    if answer1b == 'Gumdrop' or 'Gumdrops':
        spotb += 6
        print("Correct " + enterplayer2 + ", you move ahead 6 steps!")
    else :
        print("Sorry " + enterplayer2 + ", the answer was Gumdrop. You don't get to move ahead any spaces.")
    print("Current spot: " + enterplayer2 + " : " + str(spotb))

    while round < 2 and (answer2 != 'Butterfinger'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer2 = input('Keep your hands off of my ____________! (Nestle Brand)\n>')
        answer2 = answer2.capitalize()
        print(f"Round: {round} for {enterplayer2}")
        answer2b = input('Keep your hands off of my ____________! (Nestle Brand)\n>')
        answer2b = answer2b.capitalize()
    if answer2 =='Butterfinger':
        spot += 12
        print("Correct " + enterplayer1 + ", you move ahead 12 steps!")
    else :
        print("Sorry " + enterplayer1 + ", the answer was Butterfinger. You move back 6 spaces to the beginning.")
        spot = 0
    print("Current spot: " + enterplayer1 + " : "+ str(spot))
    if answer2b =='Butterfinger':
        spotb += 12
        print("Correct " + enterplayer2 + ", you move ahead 12 steps!")
    else :
        print("Sorry " + enterplayer2 + ", the answer was Butterfinger. You move back 6 spaces to the beginning.")
        spotb = 0
    print("Current spot: " + enterplayer2 + " : " + str(spotb))

    while round < 3 and (answer3 != 'Twix'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer3 = input("____ , Two for me, none for you!\n>")
        answer3 = answer3.capitalize()
        print(f"Round: {round} for {enterplayer2}")
        answer3b = input("____ , Two for me, none for you!\n>")
        answer3b = answer3b.capitalize()
    if answer3 == 'Twix':
        spot += 4
        print("Correct " + enterplayer1 + ", you move ahead 4 steps!")
    elif (spot < 5):
        print("Sorry " + enterplayer1 + ", the answer was Twix. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry " + enterplayer1 + ", the answer was Twix. You move back 4 spaces.")
        spot -= 4
    print("Current spot: " + enterplayer1 + " : "+ str(spot))
    if answer3b == 'Twix':
        spotb += 4
        print("Correct " + enterplayer2 + ", you move ahead 4 steps!")
    elif (spotb < 5):
        print("Sorry " + enterplayer2 + ", the answer was Twix. You are lagging at the beginning of the game.")
        spotb = 0
    else :
        print("Sorry " + enterplayer2 + ", the answer was Twix. You move back 4 spaces.")
        spotb -= 4
    print("Current spot: " + enterplayer2 + " : " + str(spotb))

    while round < 4 and (answer4 != 'Skittles'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer4 = input("________ , taste the rainbow!\n>")
        answer4 = answer4.capitalize()
        print(f"Round: {round} for {enterplayer2}")
        answer4b = input("________ , taste the rainbow!\n>")
        answer4b = answer4b.capitalize()
    if answer4 == 'Skittles':
        spot += 8
        print("Correct " + enterplayer1 + ", you move ahead 8 steps!")
    elif (spot < 9):
        print("Sorry " + enterplayer1 + ", the answer was Skittles. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry " + enterplayer1 + ", the answer was Skittles. You move back 8 spaces.")
        spot -= 8
    print("Current spot: " + enterplayer1 + " : "+ str(spot))
    if answer4b == 'Skittles':
        spotb += 8
        print("Correct " + enterplayer2 + ", you move ahead 8 steps!")
    elif (spotb < 9):
        print("Sorry " + enterplayer2 + ", the answer was Skittles. You are lagging at the beginning of the game.")
        spotb = 0
    else :
        print("Sorry " + enterplayer2 + ", the answer was Skittles. You move back 8 spaces.")
        spotb -= 8
    print("Current spot: " + enterplayer2 + " : " + str(spotb))

    while round < 5 and (answer5 != 'York'):
        round += 1
        print(f"Round: {round} for {enterplayer1}")
        answer5 = input("Round pepperment pattie with dark chocolate on the outside. Shiny silver Packaging.\n>")
        answer5 = answer5.capitalize()
        print(f"Round: {round} for {enterplayer2}")
        answer5b = input("Round pepperment pattie with dark chocolate on the outside. Shiny silver Packaging.\n>")
        answer5b = answer5b.capitalize()
    if answer5 == 'York':
        spot += 4
        print("Correct " + enterplayer1 + ", you move ahead 4 steps!")
    elif (spot < 5):
        print("Sorry " + enterplayer1 + ", the answer was York. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry " + enterplayer1 + ", the answer was Twix. You move back 4 spaces.")
        spot -= 4
    print("Current spot: " + enterplayer1 + " : "+ str(spot))
    if answer5b == 'York':
        spotb += 4
        print("Correct " + enterplayer2 + ", you move ahead 4 steps!")
    elif (spotb < 5):
        print("Sorry " + enterplayer2 + ", the answer was York. You are lagging at the beginning of the game.")
        spotb = 0
    else :
        print("Sorry " + enterplayer2 + ", the answer was Twix. You move back 4 spaces.")
        spotb -= 4
    print("Current spot: " + enterplayer2 + " : " + str(spotb))
    if (spot > 25):
        print(enterplayer1 + ", you have saved the land of candy from all of the children who conspire to erode the contents of this magical kingdom. Congratulations!")
        print(f"Final Score: {enterplayer1} : {spot}")
    if (spot < 25):
        print(enterplayer1 + ", you have failed to reach the point of saving the Candy Kingdom. Better luck next time!")
        print(f"Final Score: {enterplayer1} : {spot}")
    if (spotb > 25):
        print(enterplayer2 + ", you have saved the land of candy from all of the children who conspire to erode the contents of this magical kingdom. Congratulations!")
        print(f"Final Score: {enterplayer2} : {spotb}")
    if (spotb < 25):
        print(enterplayer2 + ", you have failed to reach the point of saving the Candy Kingdom. Better luck next time!")
        print(f"Final Score: {enterplayer2} : {spotb}")
        print(gameover)