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
        strip[i] = (255,179,0)
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


def showMessageU(nextMessage,duration,myMessage,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint



    i = 0
    for r in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
        for c in range(0,8):
            temp = r % len(myMessage)
            color = myMessage[temp][c]
            lookupColor(color,i)
            i += 1

    for r in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
        for c in range(8,16):
            temp = r % len(myMessage)
            color = myMessage[temp][c]
            lookupColor(color,i)
            i += 1

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
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageU(2,13,globalvariables.message1,0)


    elif globalvariables.messageID == 2:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageU(3,10,globalvariables.message2,0)


    elif globalvariables.messageID == 3:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageU(4,3,globalvariables.message2,10)


    elif globalvariables.messageID == 4:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageU(1,15,globalvariables.message1,4)
