# Tutorial 3.1
# CircuitPython demo - NeoPixel
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness a low value 0.2
    strip.brightness = 0.2
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)

    # increase brightness to 0.4
    strip.brightness = 0.4
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)

    # increase brightness to 0.6
    strip.brightness = 0.6
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)

    # increase brightness to 0.8
    strip.brightness = 0.8
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)

    # increase brightness to 0.0
    strip.brightness = 0.0
    strip[0] = (255,0,0)
    strip.write()
    time.sleep(1)