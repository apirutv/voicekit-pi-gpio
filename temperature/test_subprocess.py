#!/usr/bin/env python3

import sys
import subprocess


SUB_PATH = "/home/pi/python/voicekit-pi-gpio"

process = SUB_PATH + "/temperature/read_temp.py 22 12"

print("running " + process + " ...")
result = subprocess.check_output(process , shell=True)
values = result.decode('utf-8').strip().split("|")
print(values)
#sys.exit(0)
