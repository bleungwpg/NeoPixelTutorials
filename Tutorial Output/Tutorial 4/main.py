# Tutorial 4.1
# CircuitPython demo - NeoPixel
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    strip.brightness = 0.4

    # set color to red
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)

    # set color to green
    strip[0] = (0,255,0)
    strip.write()
    time.sleep(1)

    # set color to blue
    strip[0] = (0,0,255)
    strip.write()
    time.sleep(1)

    # set color to orange
    strip[0] = (125,255,0)
    strip.write()
    time.sleep(1)

    # set color to light blue
    strip[0] = (102,228,247)
    strip.write()
    time.sleep(1)