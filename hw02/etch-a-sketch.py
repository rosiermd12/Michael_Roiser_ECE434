#!/user/bin/env python

#Author: Michael Rosier
#Date: 9/11/2018
#
#discription:
#This program makes an etch-a-sketch game on the terminal
#that can be any size. 
#
#How it works:
#when promted about the size, just put a number of
#rows or colums you want (this makes an n by n grid).
#
#after determining the grid size, you will see a 
#grid of '_' with one 'X' and you will move the cursor
#left, right, up, or down through buttons on pins P9_11,
#P9_13, P9_15, and P9_17.

from os import system
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_15", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)

GPIO.add_event_detect("P9_11", GPIO.RISING)
GPIO.add_event_detect("P9_13", GPIO.RISING)
GPIO.add_event_detect("P9_15", GPIO.RISING)
GPIO.add_event_detect("P9_17", GPIO.RISING)
#variables
posX = 0
posY = 0
array = ['X']
n = 0

#setgrid function 

def setgrid(gridmap,num):
    for y in range(num*num):
        gridmap.extend('_')
    return

#clear array function 

def clearArray(gridmap,num):
    for y in range(num*num):
        gridmap.pop(len(gridmap)-1)
    return

#display function
def display(stuff,w):
    m = 0
    for x in range(len(stuff)):
        if m > w-1:
            m = 1
            print ""
            if x != n*n:
                print stuff[x],
        else:
            print stuff[x],
            m = m+1 
    return  
 #start         
print("etch-a-sketch size>"),
n = input()
setgrid(array,n)
display(array,n)

#switch method

def switch():
    global posX
    global posY
    if GPIO.event_detected("P9_15"):
        posY -= 1
        if posY  < 0:
            posY = n-1
            
    elif GPIO.event_detected("P9_17"):
        posY += 1
        if posY  > n-1:
            posY = 0
            
    elif GPIO.event_detected("P9_11"):
        posX -= 1
        if posX  < 0:
            posX = n-1
            
    elif GPIO.event_detected("P9_13"):
        posX += 1
        if posX  > n-1:
            posX = 0
            
    else:
        return
    print("\033[H\033[J")
    array[posX+posY*n] = 'X'
    display(array,n)
    print('cursor <posX,posY>'),
    print(str(posX) + " " + str(posY))
    return

#_______

while True:
 switch()
 time.sleep(0.2)

 


  