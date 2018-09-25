//date: 9/24/2018
//Author: Michael Rosier

//discription:
//this program turns on USR3 and USR1 lights on the beagleboard by using mmap

#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h> 


#define USR1 (1<<22)
#define USR3 (1<<24)
#define GPIO1_SIZE (0x4804CFFF - 0x4804C000)
int main(int argc, char *argv[]) {
    volatile void *gpio_add;
    volatile unsigned int *gpio_oe;
    volatile unsigned int *gpio_setdata;
    volatile unsigned int *gpio_cleardata;
    unsigned int regist;
    
    int fd = open("/dev/mem", O_RDWR);
    
    gpio_add = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0x4804C000);

    gpio_oe  = gpio_add + 0x134;
    gpio_setdata   = gpio_add + 0x194;
    gpio_cleardata = gpio_add + 0x190;
    
    regist = *gpio_oe;
    regist &= ~USR3;       
    *gpio_oe = regist;
    
    regist = *gpio_oe;
    regist &= ~USR1;       
    *gpio_oe = regist;
    
    *gpio_setdata = USR3;
    *gpio_setdata = USR1;
    
    usleep(2000000);
    
    *gpio_cleardata = USR3;
    *gpio_cleardata = USR1;
    
    munmap((void *)gpio_add, GPIO1_SIZE);
    close(fd);
    return 0;
}