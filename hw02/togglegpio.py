#!/user/bin/env python

#Author: Michael Rosier
#Date: 9/11/2018
#
#discription:
#This program toggles an LED out of pin P8_39
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_39", GPIO.OUT)

while True:
    GPIO.output("P8_39", GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output("P8_39", GPIO.LOW)
    time.sleep(0.01)