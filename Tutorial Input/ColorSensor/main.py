import analogio
import board
import neopixel

pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
light = analogio.AnalogIn(board.LIGHT)

while True:
    pixels[1] = (255, 0, 0)
    raw_red = light.value
    red = int(raw_red * (255 / 65535))

    pixels[1] = (0, 255, 0)
    raw_green = light.value
    green = int(raw_green * (255 / 65535))

    pixels[1] = (0, 0, 255)
    raw_blue = light.value
    blue = int(raw_blue * (255 / 65535))

    strip[7] = (red,green,blue)
    strip.write()

    if red > green:
        strip[15] = (255,0,0)
    else:
        strip[15] = (0,0,0)


    if green > red:
        strip[23] = (0,255,0)
    else:
        strip[23] = (0,0,0)


    if blue > red:
        strip[31] = (0,0,255)
    else:
        strip[31] = (0,0,0)


#    if red < 100 and blue < 100 and green < 100:
#        for x in range(0,128):
#            strip[x] = (20,20,20)
#    elif red >= green && red >= blue:
#        for x in range(0,128):
#            strip[x] = (100,0,0)
#    elif green >= red && green >= blue:
#        for x in range(0,128):
#            strip[x] = (0,255,0)
#    elif blue >= red && blue >= green:
#        for x in range(0,128):
#            strip[x] = (0,255,0)
