import random

color = random.randint(1,7)

if color == 1:
    color = "yellow"
    
if color == 2:
    color = "green"
    
if color == 3:
    color = "blue"
    
if color == 4:
    color = "turquoise"
    
if color == 5:
    color = "purple"
    
if color == 6:
    color = "pink"
    
user_choice = input("Choose a color!")

if user_choice == color:
    print("good job! you guessed correctly")
else:
    print("Sorry!! That's incorrect") 