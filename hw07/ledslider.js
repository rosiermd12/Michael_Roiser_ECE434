#!/usr/bin/env node
// From Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED1 = 'P9_16';
b.pinMode(LED1, b.OUTPUT);

const AUTH = '9578cef5555d4781aa5ca6ecbae987b6';

var blynk = new Blynk.Blynk(AUTH);

var duty_cycle = new blynk.VirtualPin(0);


duty_cycle.on('write', function(param) {
    console.log('V0:', param[0]);
    b.analogWrite(LED1, param[0]);
});

