#!/usr/bin/env python3

from gpiozero import Servo
from time import sleep
servo = Servo(24)

try:
    servo.detach()

    while(True):
        value = float(input("enter servo value from -1.0 to 1.0: "))
        servo.value = value 
        print(servo.value)
        input("press a key to stop ...")
        servo.detach()

except Exception as e:
    print("ERROR",e)

