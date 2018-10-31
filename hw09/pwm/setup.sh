#!/bin/bash
export PRUN=0
export TARGET=pwm
echo PRUN=$PRUN
echo TARGET=$TARGET

echo none > /sys/class/leds/beaglebone\:green\:usr3/trigger

config-pin P9_27 pruout

