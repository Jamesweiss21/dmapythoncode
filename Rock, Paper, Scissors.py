import random

computers = random.randint(1,3)

if computers == 1:
    computers = "paper"
    
if computers == 2:
    computers = "scissors"
    
if computers == 3:
    computers = "rock"
    
    
userchoice = input("choose rock, paper, or scissors!")

    
if computers == "paper" and userchoice == "rock":
    print("you loose!")
    
    
if computers == "rock" and userchoice == "paper":
    print("you win!")
    

if computers == "paper" and userchoice == "scissors":
    print("you win!")
    
    
if computers == "rock" and userchooice == "scissors":
    print("you loose!")


if computers == "scissors" and userchoice == "rock":
    print("you win!")
    
    
if computers == "scissors" and userchoice == "paper":
    print("you loose!")
    

    
    