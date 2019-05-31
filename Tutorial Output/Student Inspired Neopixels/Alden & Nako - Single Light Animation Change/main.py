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
        strip[i] = (50,50,0)
    # green
    elif color == 13:
        strip[i] = (0,50,0)
    # blue
    elif color == 14:
        strip[i] = (0,0,255)
    # violet
    elif color == 15:
        strip[i] = (62,0,105)
    # red
    elif color == 17:
        strip[i] = (255,0,0)
    # white
    elif color == 18:
        strip[i] = (0,0,0)
    # grey
    elif color == 19:
        strip[i] = (56,56,56)

# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def showMessagePattern(nextMessage,duration,myMessage,pattern,startingPoint):
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


    for r in range(0,globalvariables.countToMaxLength):
        lookupColor(pattern[1][r],pattern[0][r])


    strip.write()

    globalvariables.countToMaxLength += 1
    globalvariables.durationCounter += 1
    if globalvariables.durationCounter > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage




def showMessageL(nextMessage,duration,myMessage,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    strip.write()

    globalvariables.countToMaxLength += 1
    globalvariables.durationCounter += 1
    if globalvariables.countToMaxLength > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage


def showMessage(nextMessage,duration,myMessage):
    # start - fixed message 4
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = nextMessage


# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    if globalvariables.messageID == 1:
        # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
        showMessagePattern(1,40,globalvariables.message1,globalvariables.pattern1,0)
