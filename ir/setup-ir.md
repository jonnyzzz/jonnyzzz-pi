#!/bin/bash

set -e -x -u

## see http://ozzmaker.com/how-to-control-the-gpio-on-a-raspberry-pi-with-an-ir-remote/

sudo apt-get install lirc liblircclient-dev

## See https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry-pi-circuit-note.html

GPIO_PIN=18

## add to /ect/modules 
# lirc_dev
# lirc_rpi gpio_in_pin=18

## add to /boot/config.txt 
# dtoverlay=lirc-rpi,gpio_in_pin=18 
#

https://raspberrypi.stackexchange.com/questions/81876/raspberry-pi-3-not-lirc-not-running-working

## gpio-ir
https://www.raspberrypi.org/forums/viewtopic.php?t=236240

