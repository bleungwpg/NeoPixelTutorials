# Tutorial 1.1
# CircuitPython demo - NeoPixel

import time

import board
import neopixel

pixpin = board.A3
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
    strip.brightness = 0.7

    strip[0] = (255,0,0)
    strip[1] = (255,0,0)
    strip[2] = (255,0,0)
    strip[3] = (255,0,0)

    strip.write()
