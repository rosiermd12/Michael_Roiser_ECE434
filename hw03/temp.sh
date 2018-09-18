#!/bin/sh
#Author: Michael Rosier
#Date: 9/17/2018
#
#discription:
#this takes the temps from the temp sensors that are connected to the i2c2 bus 
#and displays them in ferenhiet.
#
#Pins P9_20 and P9_19

while(true) do

temp=$(i2cget -y 2 0x48)
temp2=$(i2cget -y 2 0x4a)

printf "temp sensor 1\n"
printf "temp = "
a=$(($temp * 9/5 + 32))
printf $a
printf " F\n"

printf "temp sensor 2\n"
printf "temp = "
b=$(($temp2 * 9/5 + 32))
printf $b
printf " F\n"

sleep 1s
done
