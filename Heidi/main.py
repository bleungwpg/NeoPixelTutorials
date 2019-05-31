import globalvariables

import time
import board
import neopixel

pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 0:
        strip[i] = (0,0,0)
    elif color == 1:
        strip[i] = (100,100,100)

    elif color == 10:
        strip[i] = (0,0,0)

    elif color == 11:
        strip[i] = (252,0,128)

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
        strip[i] = (0,163,255)

    elif color == 17:
        strip[i] = (255,186,0)

    elif color == 99:
        strip[i] = (0,0,0)


# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def mix2MessagesD(nextMessage,duration,myMessageFront,myMessageBack,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

    if globalvariables.q <= len(myMessageBack)*-1:
        globalvariables.q = 0



    i = 0
    # start - fixed message 4
    # remember to change globalvariables.message#
    for r in range(globalvariables.q,globalvariables.q+8):
        for c in range(0,8):
            color = myMessageBack[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(globalvariables.q,globalvariables.q+8):
        for c in range(8,16):
            color = myMessageBack[r][c]
            lookupColor(color,i)
            i += 1



    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = myMessageFront[r][c]
            if color != 99:
                lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = myMessageFront[r][c]
            if color != 99:
                lookupColor(color,i)
            i += 1
    strip.write()

    globalvariables.countToMaxLength -= 1
    globalvariables.durationCounter += 1
    globalvariables.q -= 1
    if globalvariables.durationCounter > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage





# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    if globalvariables.messageID == 1:
        mix2MessagesD(1,100,globalvariables.messageFront,globalvariables.messageBack,0)
