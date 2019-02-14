# Tutorial 3.1
# CircuitPython demo - NeoPixel

import time
import board
import neopixel

pixpin = board.A3
numpix = 128

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set color to red
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)

    # set color to black / turn off light
    strip[0] = (0,0,0)
    strip.write()
    time.sleep(1)

    # set color to green
    strip[7] = (0,255,0)
    strip[64] = (0,255,0)
    strip.write()
    time.sleep(1)

    # set color to black / turn off light
    strip[7] = (0,0,0)
    strip[64] = (0,0,0)
    strip.write()
    time.sleep(1)


    # set color to blue
    strip[71] = (0,0,255)
    strip.write()
    time.sleep(1)

    # set color to black / turn off light
    strip[71] = (0,0,0)
    strip.write()
    time.sleep(1)


    # set color to orange
    strip[127] = (255,125,0)
    strip.write()
    time.sleep(1)

    # set color to black / turn off light
    strip[127] = (0,0,0)
    strip.write()
    time.sleep(1)


    # set color to white
    strip[63] = (255,255,255)
    strip[120] = (255,255,255)
    strip.write()
    time.sleep(1)

    # set color to black / turn off light
    strip[63] = (0,0,0)
    strip[120] = (0,0,0)
    strip.write()
    time.sleep(1)


    # set color to light pink
    strip[56] = (255,102,255)
    strip.write()
    time.sleep(1)

    # set color to black / turn off light
    strip[56] = (0,0,0)
    strip.write()
    time.sleep(1)
