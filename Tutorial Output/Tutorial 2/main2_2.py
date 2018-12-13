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
    # row 1
    strip[0] = (255,0,0)
    strip[1] = (255,0,0)
    strip[2] = (255,0,0)
    strip[3] = (255,0,0)
    strip[1] = (255,0,0)
    strip[5] = (255,0,0)
    strip[6] = (255,0,0)
    strip[7] = (255,0,0)

    # row 2
    strip[64-0] = (255,0,0)
    strip[64-1] = (255,0,0)
    strip[64-2] = (255,0,0)
    strip[64-3] = (255,0,0)
    strip[64-1] = (255,0,0)
    strip[64-5] = (255,0,0)
    strip[64-6] = (255,0,0)
    strip[64-7] = (255,0,0)

    # row 3
    strip[8*0] = (255,0,0)
    strip[8*1] = (255,0,0)
    strip[8*2] = (255,0,0)
    strip[8*3] = (255,0,0)
    strip[8*1] = (255,0,0)
    strip[8*5] = (255,0,0)
    strip[8*6] = (255,0,0)
    strip[8*7] = (255,0,0)

    # row 3
    strip[8*0+7] = (255,0,0)
    strip[8*1+7] = (255,0,0)
    strip[8*2+7] = (255,0,0)
    strip[8*3+7] = (255,0,0)
    strip[8*1+7] = (255,0,0)
    strip[8*5+7] = (255,0,0)
    strip[8*6+7] = (255,0,0)
    strip[8*7+7] = (255,0,0)

    strip.write()