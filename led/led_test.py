#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time


pin = int(input("enter BCM pin number: "))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)

input("press a key to turn set the pin HIGH ...")
GPIO.output(pin, GPIO.HIGH)

input("press a key to turn set the pin LOW ...")
GPIO.output(pin, GPIO.LOW)

input("press a key to end ...")

GPIO.cleanup()
