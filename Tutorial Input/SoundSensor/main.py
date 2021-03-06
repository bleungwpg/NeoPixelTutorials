import audioio
import board
import digitalio

import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

 
# enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True
 
# make the 2 input buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN
 
buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN
 
# The two files assigned to buttons A & B
audiofiles = ["danube.wav", "amazon.wav"]
 
 
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
    strip[0] = (0,0,0)
    strip.write()
    if buttonA.value:
        strip[0] = (150,0,155)
        strip.write()
        play_file(audiofiles[0])
    if buttonB.value:
        strip[0] = (0,255,0)
        strip.write()
        play_file(audiofiles[1])
