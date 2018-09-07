#!/user/bin/env python

#Author: Michael Rosier
#Date: 9/7/2018
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
#grid of '_' with one 'X' and another promt for sketch
#direction. put in the desireddirection
#
#Commands:
#right
#left
#up
#down
#clear
#exit

from os import system

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

def switch(argument):
    global posX
    global posY
    if argument == "up":
        posY -= 1
        if posY  < 0:
            posY = n-1
            
    elif argument == "down":
        posY += 1
        if posY  > n-1:
            posY = 0
            
    elif argument == "left":
        posX -= 1
        if posX  < 0:
            posX = n-1
            
    elif argument == "right":
        posX += 1
        if posX  > n-1:
            posX = 0
            
    elif argument == "exit":
        return
    elif argument == "clear":
        clearArray(array,n)
        setgrid(array,n)
    else:
        return
    array[posX+posY*n] = 'X'
    return

#_______

arg = ""
while arg != "exit":
 print("> "),
 arg = raw_input()
 system('clear')
 switch(arg)
 display(array,n)
 print('cursor <posX,posY>'),
 print(str(posX) + " " + str(posY))

 


  