import globalvariables
import analogio
import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128
light = analogio.AnalogIn(board.LIGHT)


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




# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    if light.value > 5:
        if globalvariables.messageID == 1:
            # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
            showMessagePattern(1,14,globalvariables.message3,globalvariables.pattern1,0)
    else:
        for x in range(0,128)
            strip[x] = (0,0,0)
        strip.write()
