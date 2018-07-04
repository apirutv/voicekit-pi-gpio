#!/usr/bin/python3

from lcd_i2c import *
import subprocess

ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
ip_address = ip_address.decode('utf-8').strip()

print("[" + ip_address + "]")

lcd_init()
lcd_string("Hello world !!", LCD_LINE_1)
lcd_string(ip_address, LCD_LINE_2)
