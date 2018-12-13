# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
 
import board
import neopixel
 
pixpin = board.D0
numpix = 64

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

while True:

    # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
    strip.brightness = 0.7
    
    # row 1
    strip[8*0+0] = (255,0,0)
    strip[8*1+1] = (255,0,0)
    strip[8*2+2] = (255,0,0)
    strip[8*3+3] = (255,0,0)
    strip[8*4+4] = (255,0,0)
    strip[8*5+5] = (255,0,0)
    strip[8*6+6] = (255,0,0)
    strip[8*7+7] = (255,0,0)

    # row 2
    strip[8*0+7] = (255,0,0)
    strip[8*1+6] = (255,0,0)
    strip[8*2+5] = (255,0,0)
    strip[8*3+4] = (255,0,0)
    strip[8*4+3] = (255,0,0)
    strip[8*5+2] = (255,0,0)
    strip[8*6+1] = (255,0,0)
    strip[8*7+0] = (255,0,0)


    strip.write()