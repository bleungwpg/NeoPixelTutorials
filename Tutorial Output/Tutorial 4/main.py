# Tutorial 4.1
# CircuitPython demo - NeoPixel

import time
import board
import neopixel

pixpin = board.A3
numpix = 128

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    strip[0] = (50,0,0)
    strip.write()
    time.sleep(1)

    strip[1] = (100,0,0)
    strip.write()
    time.sleep(1)

    strip[2] = (150,0,0)
    strip.write()
    time.sleep(1)

    strip[3] = (200,0,0)
    strip.write()
    time.sleep(1)

    strip[4] = (255,0,0)
    strip.write()
    time.sleep(1)

    for x in range(0,5)
        strip[x] = (0,0,0)
    strip.write()
    time.sleep(2)
