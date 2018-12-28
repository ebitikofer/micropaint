from microbit import *
# import random

oneDice = Image("03030:"
                "36363:"
                "36963:"
                "03630:"
                "00300")
                
blankScreen = Image("00000:"
                    "00000:"
                    "00000:"
                    "00000:"
                    "00000")

cursorPosition = [2, 2, 5]
velocity = [0, 0, 0]
priorValue = 9
zDir = 0

sensitivity = 100
incrX = 0
incrY = 0

def moveCursor(incrementX, incrementY):
    cursorPosition[0] += incrementX
    if cursorPosition[0] > 4:
        cursorPosition[0] = 0
    if cursorPosition[0] < 0:
        cursorPosition[0] = 4
    
    cursorPosition[1] += incrementY
    if cursorPosition[1] > 4:
        cursorPosition[1] = 0
    if cursorPosition[1] < 0:
        cursorPosition[1] = 4

display.show(oneDice)

while True:
    
    velocity = accelerometer.get_values()
    
    if velocity[0] > sensitivity:
        incrX = 1
    elif velocity[0] < -sensitivity:
        incrX = -1
    else:
        incrX = 0
        
    if velocity[1] > sensitivity:
        incrY = 1
    elif velocity[1] < -sensitivity:
        incrY = -1
    else:
        incrY = 0
    
    # if button_a.was_pressed() and button_b.was_pressed():
        # priorValue = 0
    # el
    if button_a.was_pressed():
        priorValue -= 3
        if priorValue < 0:
            priorValue = 0
    elif button_b.was_pressed():
        priorValue += 3
        if priorValue > 9:
            priorValue = 9
    
    if incrX != 0 or incrY != 0:
        # reset the current pixel to it's initial state
        display.set_pixel(cursorPosition[0], cursorPosition[1], priorValue)
        
        # move the cursor 
        moveCursor(incrX, incrY)
        
        # record the current value of the pixel at the cursor destination
        priorValue = display.get_pixel(cursorPosition[0], cursorPosition[1])
        
        # write cursor value to the new position
        zDir = 0
        cursorPosition[2] = 9
        display.set_pixel(cursorPosition[0], cursorPosition[1], cursorPosition[2])
        sleep(500)
    else:
        if zDir == 0:
            cursorPosition[2] -= 1
            if cursorPosition[2] < 0:
                cursorPosition[2] = 0
                zDir = 1
        elif zDir == 1:
            cursorPosition[2] += 1
            if cursorPosition[2] > 9:
                cursorPosition[2] = 9
                zDir = 0
        display.set_pixel(cursorPosition[0], cursorPosition[1], cursorPosition[2])
        # random.randint(1, 7))
        sleep(50)