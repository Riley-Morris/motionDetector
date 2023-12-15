import time
from picamera2 import Picamera2, Preview
from gpiozero import MotionSensor
from signal import pause

import RPi.GPIO as GPIO

import simpleaudio as sa

picam = Picamera2()
pir=MotionSensor(19)

config = picam.create_preview_configuration()
picam.configure(config)


def buzzerGo():
    print('start buzzer')
    backOff = 'backOff.wav' #filename and path
    audioObj = sa.WaveObject.from_wave_file(backOff)#create audio object from simpleaudio functions
    play_obj = audioObj.play()
    play_obj.wait_done() #wait for sound to finish before closing
    print('end buzzer')
   
#turns camera on for 10 seconds
#To do: add functionality to save video recording
def modulesGo():
    print('MOTION DETECTED')
    picam.start_preview(Preview.QTGL)
    picam.start() #start camera
    buzzerGo() #start audio
    time.sleep(5)
    picam.stop_preview()
    picam.close()
        
            
pir.when_motion=modulesGo     
pause()
