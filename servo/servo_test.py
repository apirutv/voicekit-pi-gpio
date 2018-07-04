#!/usr/bin/env python3

from gpiozero import Servo
from time import sleep
servo = Servo(24)

try:
    servo.detach()

    input("press a key to start turning to min ...")
    print("servo to min")
    servo.min()
    input("press a key to stop ...")
    servo.detach()

    input("press a key to start turning to max ...")
    print("servo to max")
    servo.max()
    input("press a key to stop ...")
    servo.detach()

except Exception as e:
    print("ERROR",e)

