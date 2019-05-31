import globalvariables

import time
import board
import neopixel

pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 10:
        strip[i] = (0,0,0)

    elif color == 11:
        strip[i] = (25,0,0)

    elif color == 12:
        strip[i] = (252,0,83)

    elif color == 13:
        strip[i] = (252,37,37)

    elif color == 14:
        strip[i] = (255,96,0)

    elif color == 15:
        strip[i] = (255,129,0)
# your color 16 did not exist
    elif color == 16:
        strip[i] = (255,163,0)

    elif color == 17:
        strip[i] = (255,186,0)

# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def showMessageFixedBackMovingRFront(nextMessage,duration,fixedBackMSG,movingFrontMSG,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

    i = 0
    for r in range(0,8):
        for c in range(0,8):
            temp = r % len(fixedBackMSG)
            color = fixedBackMSG[temp][c]
            lookupColor(color,i)
            i += 1


    for r in range(0,8):
        for c in range(8,16):
            temp = r % len(fixedBackMSG)
            color = fixedBackMSG[temp][c]
            lookupColor(color,i)
            i += 1


    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % len(movingFrontMSG[0])
            color = movingFrontMSG[r][temp]
            if color != 99:
                lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % len(movingFrontMSG[0])
            color = movingFrontMSG[r][temp]
            if color != 99:
                lookupColor(color,i)
            i += 1



    strip.write()


    globalvariables.countToMaxLength -= 1
    globalvariables.durationCounter += 1
    if globalvariables.durationCounter > duration:
        globalvariables.countToMaxRow = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage




# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    if globalvariables.messageID == 1:
        # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
        showMessageFixedBackMovingRFront(1,40,globalvariables.fixedBackMSG,globalvariables.movingFrontMSG,40)
