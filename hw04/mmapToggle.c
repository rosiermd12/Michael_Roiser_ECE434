//date: 9/24/2018
//Author: Michael Rosier

//discription:
//this program toggles USR3 light on the beagleboard by using mmap



#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h> 


#define USR1 (1<<22)
#define USR3 (1<<24)
#define GPIO1_SIZE (0x4804CFFF - 0x4804C000)


int running = 1;   

void controlC(int sig);

void controlC(int sig)
{
	running = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_add;
    volatile unsigned int *gpio_oe;
    volatile unsigned int *gpio_set;
    volatile unsigned int *gpio_clear;
    unsigned int regist;
    
    signal(SIGINT, controlC);

    int fd = open("/dev/mem", O_RDWR);
    
    gpio_add = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0x4804C000);

    gpio_oe  = gpio_add + 0x134;
    gpio_set   = gpio_add + 0x194;
    gpio_clear = gpio_add + 0x190;
    
    regist = *gpio_oe;
    regist &= ~USR3;       
    *gpio_oe = regist;
    
    while(running) {
        //printf("on\n");
        *gpio_set = USR3;
        usleep(250000);
        
        //printf("off\n");
        *gpio_clear = USR3;
        usleep(250000);
    }
    
    munmap((void *)gpio_add, GPIO1_SIZE);
    close(fd);
    return 0;
}