import globalvariables

import time
import board
import neopixel

pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def showMessage1():
	# reset previous colors
    strip[96] = (0,0,0)
    strip[103] = (0,0,0)

    # show color
    strip[0] = (255,0,0)
    strip[7] = (255,0,0)
    strip.write()
    time.sleep(1)

    # switch to next message
    globalvariables.messageID = 2




def showMessage2(nextMessage):
	# reset previous colors
    strip[0] = (0,0,0)
    strip[7] = (0,0,0)

    # show color
    strip[32] = (0,255,0)
    strip[39] = (0,255,0)
    strip.write()
    time.sleep(2)

    # switch to next message
    globalvariables.messageID = nextMessage



def showMessage3(duration):
	# reset previous colors
    strip[32] = (0,0,0)
    strip[39] = (0,0,0)

    # show color
    strip[64] = (255,50,200)
    strip[71] = (255,50,200)
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = 4



def showMessage4(nextMessage,duration):
	# reset previous colors
    strip[64] = (0,0,0)
    strip[71] = (0,0,0)

    # show color
    strip[96] = (0,0,255)
    strip[103] = (0,0,255)
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = nextMessage



while True:
    if globalvariables.messageID == 1:
        # call function showMessage1()
        showMessage1()


    elif globalvariables.messageID == 2:
        # call function showMessage2(nextMessage)
        showMessage2(3)


    elif globalvariables.messageID == 3:
        # call function showMessage3(messageDuration)
        showMessage3(1)


    elif globalvariables.messageID == 4:
        # call function showMessage4(nextMessage,messageDuration)
        showMessage4(1,2)

