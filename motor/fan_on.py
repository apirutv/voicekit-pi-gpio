#!/usr/bin/env python3

from gpiozero import PWMOutputDevice
from time import sleep

PWM_DEVICE = 4

pwm = PWMOutputDevice(PWM_DEVICE)

print("turnin PWM " + str(PWM_DEVICE) + " on for 10 seconds ...")
pwm.on()
sleep(10)
print("turnin PWM " + str(PWM_DEVICE) + " off")
pwm.off()
