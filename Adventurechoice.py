import random
choices = ["A" , "B"]
print("you're stuck in a room with two doors, which door will you go into?")
userchoice = input("Make a choice... type 1 to go into the red door, type 2 to go into the blue door!")
if userchoice == "1":
    ud2 = input("you fell into a pool of lava, luckily you have a shield to protect you! Choose a direction to go, left or right")
if userchoice == "2":
    ud2 = input("you swam into a sea full of sharks, fortunately you have found a shark cage to protect you! Choose a direction to go, left or right")
    if ud2 == "left":
        print("You climbed out of the lava! You take the next bus home and you are now safe! Congradulations!")
    if ud2 == "right":
        print("Oh No! You took a wrong turn and fell down a waterfall of lava! You loose!")
    if ud2 == "left":
        print("Oh No! You took the wrong turn and got eaten by a great white shark! You loose!")
    if ud2 == "right":
        print("You outswam the sharks and made it to saftey! Congrats! You go back to your home, you are now safe!")