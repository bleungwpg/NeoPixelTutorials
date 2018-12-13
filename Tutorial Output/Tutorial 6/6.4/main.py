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
    # orange
    elif color == 11:
        strip[i] = (50,79,0)
    # yellow
    elif color == 12:
        strip[i] = (255,255,0)
    # green
    elif color == 13:
        strip[i] = (0,255,0)
    # blue
    elif color == 14:
        strip[i] = (0,0,255)
    # violet
    elif color == 15:
        strip[i] = (62,0,105)
    # red
    elif color == 17:
        strip[i] = (255,0,0)


# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def showMessageMaskD(nextMessage,duration,myMessage,mask,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint


    i = 0
    r = globalvariables.countToMaxLength
    r2 = 0
    while r2 < 8:
        for c in range(0,8):
            temp = r % len(myMessage)
            color = myMessage[temp][c]
            if mask[r2][c] == 1:
                lookupColor(color,i)
            else:
                strip[i] = (0,0,0)
            i += 1
        r2 += 1
        r += 1

    r = globalvariables.countToMaxLength
    r2 = 0
    while r2 < 8:
        for c in range(8,16):
            temp = r % len(myMessage)
            color = myMessage[temp][c]
            if mask[r2][c] == 1:
                lookupColor(color,i)
            else:
                strip[i] = (0,0,0)
            i += 1
        r2 += 1
        r += 1

    strip.write()

    globalvariables.countToMaxLength += 1
    globalvariables.durationCounter += 1
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
        # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
        showMessageMaskD(2,20,globalvariables.message4,globalvariables.mask1,0)
    elif globalvariables.messageID == 2:
        # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
        showMessageMaskD(1,20,globalvariables.message3,globalvariables.mask1,0)