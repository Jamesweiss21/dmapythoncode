##traffic_light

from gpiozero import LED
from time import sleep

red = LED(4)
yellow = LED(17)
green = LED(27)
while True:
    red.on()
    sleep(2)
    red.off()


    yellow.on()
    sleep(2)
    yellow.off()

    green.on()
    sleep(2)
    green.off()
    break
    
    
userchoice = input("Choose a color on the stoplight!")

if userchoice == "red":
    red.on()
    sleep(2)
    red.off()
    
    
if userchoice == "yellow":
    yellow.on()
    sleep(2)
    yellow.off()
    
    
if userchoice == "green":
    green.on()
    sleep(2)
    green.off()
    
    
    
    