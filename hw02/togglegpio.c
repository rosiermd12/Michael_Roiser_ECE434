//!/user/bin/env C
//Author: Michael Rosier
//Date: 9/11/2018
//
//discription:
//This program toggles an LED out of pin P8_39
//
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "gpio_utils.h"

int main() {
    int pin = 76;
    
    FILE *io, *iodir, *ioval;
    
    gpio_export(pin);
    
    gpio_set_dir(pin, "out");
    
    int gpio_fd = gpio_fd_open(pin, O_RDONLY);
    
    while(1) {
        gpio_set_value(pin, 1);
        
        usleep(100000);
        
        gpio_set_value(pin, 0);
        
        usleep(100000);
    }
    
    gpio_fd_close(gpio_fd);
    return 0;
}