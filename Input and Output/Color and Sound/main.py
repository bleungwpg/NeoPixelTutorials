import analogio
import audioio
import digitalio
import board
import neopixel

pixpin = board.A3
numpix = 128

color = 0
counter = 0
correct = 0


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
light = analogio.AnalogIn(board.LIGHT)

# enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# The two files assigned to buttons A & B
audiofiles = ["danube.wav", "amazon.wav", "nile.wav", "yangtze.wav"]
 
 
def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")


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

    print("Red"+str(raw_red)+"     Green"+str(raw_green)+"        Blue"+str(raw_blue))
    

    strip[7] = (red,green,blue)
    strip.write()

    if red < 17 and blue < 17 and green < 17:
        color = 0
    elif red > green and red > blue:
        color = 1
    elif green > red and raw_green-raw_blue > 200:
        color = 2
    elif blue > red and green > red:
        color = 3

    #nile
    if color == 1:
        strip[15] = (255,0,0)
#        play_file(audiofiles[2])
        counter += 1
        if correct == 0 and counter == 1:
            correct += 1
    else:
        strip[15] = (0,0,0)


    # amazon
    if color == 2:
        strip[23] = (0,255,0)
#        play_file(audiofiles[1])
        counter += 1
        if correct == 1 and counter == 2:
            correct += 1
    else:
        strip[23] = (0,0,0)

    # danube
    if color == 3:
        strip[31] = (0,0,255)
#        play_file(audiofiles[0])
        counter += 1
        if correct == 2 and counter == 3:
            correct += 1
    else:
        strip[31] = (0,0,0)


    if counter == 3 and correct == 3:
        pixels[5] = (255,0,0)
        counter = 0
        correct = 0
    elif counter == 3:
        counter = 0
        correct = 0
