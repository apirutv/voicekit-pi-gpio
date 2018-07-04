#!/usr/bin/env python3

from gpiozero import PWMOutputDevice
from time import sleep
pwm = PWMOutputDevice(4)
while True:
    input("press a key to turn the motor on ...")
    pwm.on()
    input("press a key to stop ...")
    pwm.off()

    input("press a key to turn the motor on half speed ...")
    pwm.value = 0.5
    input("press a key to stop ...")
    pwm.value = 0.0
