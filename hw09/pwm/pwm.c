#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
        uint32_t gpio;

        /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
        CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

        gpio= 0x1<<5;

        while(1) {
                __R30 |= gpio;
                __delay_cycles(10/10);    
                __R30 &= ~gpio;
                __delay_cycles(10/10); 
        }
}


