#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pins = [26,6,13,5]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

i = 0
round = 0
is_stop = False
round_num = 10 

while(not is_stop):
    #print("setting pin " + str(pins[i]) + " HIGH ...")
    GPIO.output(pins[i], GPIO.HIGH)
    time.sleep(.5)
    #print("setting pin " + str(pins[i]) + " LOW ...")
    GPIO.output(pins[i], GPIO.LOW)

    if(i >= len(pins)-1):
        i = 0
        round += 1
        #if(round >= round_num):
        #   is_stop = True 
    else:
        i += 1

GPIO.cleanup()
