#

#author: Michael Rosier
#date: 9/9/2018
#
#Discription:
#this program uses four buttons to toggle four leds on or off
#
#Pin Setup:
#Buttons: P9_11, P9_13, P9_15, P9_17
#Leds: P8_39, P8_41, P8_43
#
#Notes:
#This only works with the u-boot on the sd card. to
#boot up from the sd card instead of the eMMC you have
#to hold down the USER button before attaching the 
#beaglebone to your computer. wait until the four
#leds on the beaglebone light up all at once then you 
#can let go of the USER button.

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_15", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P8_39", GPIO.OUT)
GPIO.setup("P8_41", GPIO.OUT)
GPIO.setup("P8_43", GPIO.OUT)
GPIO.setup("P8_45", GPIO.OUT)

GPIO.add_event_detect("P9_11", GPIO.RISING)
GPIO.add_event_detect("P9_13", GPIO.RISING)
GPIO.add_event_detect("P9_15", GPIO.RISING)
GPIO.add_event_detect("P9_17", GPIO.RISING)

def interupts():
    if GPIO.event_detected("P9_11"):
        if GPIO.input("P8_39") == 0:
            GPIO.output("P8_39",GPIO.HIGH)
        else:
            GPIO.output("P8_39",GPIO.LOW)
    
    if GPIO.event_detected("P9_13"):
        if GPIO.input("P8_41") == 0:
            GPIO.output("P8_41",GPIO.HIGH)
        else:
            GPIO.output("P8_41",GPIO.LOW)
    
        
    if GPIO.event_detected("P9_15"):
        if GPIO.input("P8_43") == 0:
            GPIO.output("P8_43",GPIO.HIGH)
        else:
            GPIO.output("P8_43",GPIO.LOW)
    
    if GPIO.event_detected("P9_17"):
        if GPIO.input("P8_45") == 0:
            GPIO.output("P8_45",GPIO.HIGH)
        else:
            GPIO.output("P8_45",GPIO.LOW)
    

while True:
    interupts()
    time.sleep(0.5)