#!/bin/bash
export PRUN=0
export TARGET=toggle
echo PRUN=$PRUN
echo TARGET=$TARGET

echo none > /sys/class/leds/beaglebone\:green\:usr3/trigger

config-pin P9-27 gpio
config-pin P9-27 out
