#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

#define GPIO3 0x481AE000
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_SETDATAOUT 0x194
#define USR3 (1<<19)
unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO3_SET   = (unsigned int *) (GPIO3 + GPIO_SETDATAOUT);

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {

        /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
        CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

        while(1) {
                *GPIO3_SET = USR3;      // The the USR3 LED on
                __delay_cycles(1);    // Wait 1/2 second

                *GPIO3_CLEAR = USR3;
                __delay_cycles(1); 
        }
}
