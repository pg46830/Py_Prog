from pygame import mixer
import time
# Starting the mixer
mixer.init()
def water():
    time.sleep(10)
    # Loading the song
    mixer.music.load("water.mp3")

    # Setting the volume
    mixer.music.set_volume(1)

    # Start playing the song
    mixer.music.play()
def eye():
    time.sleep(15)
    mixer.music.load("eye_excercise.mp3")

    # Setting the volume
    mixer.music.set_volume(1)

    # Start playing the song
    mixer.music.play()
def excer():
    time.sleep(20)
    mixer.music.load("excercise.mp3")

    # Setting the volume
    mixer.music.set_volume(1)

    # Start playing the song
    mixer.music.play()
while True:
    while True:
        water()
        a=input('Enter Drank for stop')
        if a=='Drank':
            mixer.music.pause()
            break
        else:
            print('You entered wrong code')
    while True:
        eye()
        a=input('Enter Drank for stop')
        if a=='Eyex':
            mixer.music.pause()
            break
        else:
            print('You entered wrong code')
    while True:
        excer()
        a=input('Enter Drank for stop')
        if a=='Ex':
            mixer.music.pause()
            break
        else:
            print('You entered wrong code')
