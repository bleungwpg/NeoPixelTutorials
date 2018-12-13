# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 128

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


# 5.1 modify the RGB triples below
grid = [[255,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ]]
 
 
while True:

    strip.brightness = 0.1

    # 5.1
    # this is known as a for loop where the variable c takes on the values 0 - 7 one at a time.
    # each set of RGB values belongs to a column represented by the variable c
    for col in range(0,8):
      strip[col] = (grid[col][0],grid[col][1],grid[col][2])


    strip.write()
