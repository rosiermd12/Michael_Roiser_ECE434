#!/user/bin/env python

#Author: Michael Rosier
#Date: 9/17/2018
#
#discription:
#This program makes an etch-a-sketch game on a 8x8 LED matrix that is controled
#by two rotory encoders.
#

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

#sets up i2c2 bus for LED Matrix
bus = smbus.SMBus(2) 
matrix = 0x70    

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#this sets up the two rotory encoders
myEncoder = RotaryEncoder(eQEP1)
myEncoder.setAbsolute()
myEncoder.enable()

myEncoder2 = RotaryEncoder(eQEP2)
myEncoder2.setAbsolute()
myEncoder2.enable()

#variables
posX = 0
posY = 0
rotorPosX = 0
rotorPosY = 0
n = 8

#set all of the variables for the LED matrix to bianary for a better understanding of how it works
etch = [0b00000001, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,
    0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

#switch method
def switch():
    global posX
    global posY
    global rotorPosY
    global rotorPosX
    
    posX = abs((myEncoder2.position % 32)/4)
    posY = abs((myEncoder.position % 32)/4)
    etch[posX*2] = etch[posX*2] | 2 ** posY 
    bus.write_i2c_block_data(matrix, 0, etch)
    return

#_______

while True:
 switch()

 


  