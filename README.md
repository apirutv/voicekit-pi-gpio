# voicekit-pi-gpio
Using AIY voice kit to control GPIOs on Raspberry Pi

# DEPENDENCIES

installing I2C LCD

enable I2C interface on raspberry pi
sudo raspi-config

INSTALL I2C-TOOLS AND SMBUS
sudo apt-get install i2c-tools
sudo apt-get install python-smbus

http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

reading temperature sensor

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install

http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
