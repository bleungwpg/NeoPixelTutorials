# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value
    # fill the first 3 lights with different colors. Note the first light is 0
    # show for 3 seconds
    strip.brightness = 0.7
    strip[0] = (255,0,0)
    strip[1] = (255,0,0)
    strip[2] = (255,0,0)
    strip[3] = (255,0,0)
    strip[4] = (255,0,0)
    strip[5] = (255,0,0)
    strip[6] = (255,0,0)
    strip[7] = (255,0,0)
    strip.write()

