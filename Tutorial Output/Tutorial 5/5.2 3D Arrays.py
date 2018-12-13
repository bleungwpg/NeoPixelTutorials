# Y9 Demo
# CircuitPython demo - NeoPixel
 
import time
import board
import neopixel
 
pixpin = board.D0
numpix = 128

i = 0

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


# 6.2 modify the following table of RGB values
grid = [[[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ]],
        [[255,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[0  ,0  ,0  ],[255,0  ,0  ]],
        [[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ],[255,0  ,0  ]]]
 
 
while True:

    strip.brightness = 0.1

    # set/reset i to 0
    i = 0

    # the variable row represents rows 0 - 2
    for row in range(0,3):

        # the variable col represents columns 0 - 7
        for col in range(0,8):

            # translate the grid structure into increasing values represented by variable i
            # i represents the values from 0 - 23
            strip[i] = (grid[row][col][0],grid[row][col][1],grid[row][col][2])

            # increase i by 1
            i += 1


    strip.write()
