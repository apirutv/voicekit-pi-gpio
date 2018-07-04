#!/usr/bin/env python3

from gpiozero import Servo
from gpiozero import AngularServo
from time import sleep

MIN_ANGLE = -360 
MAX_ANGLE = 360 

PWM_PIN = 24

servo = AngularServo(PWM_PIN, min_angle=MIN_ANGLE, max_angle=MAX_ANGLE)

try:
    servo.detach()

    while(True):

        angle = int(input("angle a angle from " + str(MIN_ANGLE) + " to " + str(MAX_ANGLE) + ": "))

        print("turning servo on PWN " + str(PWM_PIN) + " to " + str(angle) + " ...")
        servo.angle = angle
        print("servo value = " + str(servo.value))
        servo.detach()

except Exception as e:
    print("ERROR",e)

