#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

relay_pins = [27,22]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for relay_pin in relay_pins:
    GPIO.setup(relay_pin, GPIO.OUT)
    print("turning relay pin " + str(relay_pin) + " to HIGH")
    GPIO.output(relay_pin, GPIO.HIGH)
    time.sleep(1)

time.sleep(5)

for relay_pin in relay_pins:
    print("turning relay pin " + str(relay_pin) + " to LOW")
    GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
