import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.02, auto_write=False)


def lookupColor(color,i):
    # no color
    if color == 10:
        strip[i] = (0,0,0)
   
    elif color == 11:
        strip[i] = (255,0,0)
   
    elif color == 12:
        strip[i] = (255,255,0)

    elif color == 13:
        strip[i] = (0,0,0)

    elif color == 14:
        strip[i] = (0,0,0)

    elif color == 15:
        strip[i] = (0,0,0)
    # pink
    elif color == 16:
        strip[i] = (0,0,0)
    # red
    elif color == 17:
        strip[i] = (0,0,0)
    
    elif color == 18:
        strip[i] = (0,0,0)



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



def showMessageD(nextMessage,duration,myMessage,startingPoint):
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

    globalvariables.countToMaxLength -= 1
    globalvariables.durationCounter += 1
    if globalvariables.durationCounter > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage


while True:
    if globalvariables.messageID == 1:
        # showMessage(nextMessage,messageDuration,message)
        showMessageU(2,8,globalvariables.message0,0)

    elif globalvariables.messageID == 2:
        # showMessage(nextMessage,messageDuration,message)
        showMessage(3,0,globalvariables.message1)

    elif globalvariables.messageID == 3:
        # showMessage(nextMessage,messageDuration,message)
        showMessage(4,0,globalvariables.message2)

    elif globalvariables.messageID == 4:
        # showMessage(nextMessage,messageDuration,message)
        showMessage(5,0,globalvariables.message1)

    elif globalvariables.messageID == 5:
        # showMessage(nextMessage,messageDuration,message)
        showMessage(1,0,globalvariables.message2)
