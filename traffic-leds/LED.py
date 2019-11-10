#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

PIN_R = 16
PIN_Y = 20
PIN_G = 21

PIN_ALL = [PIN_R, PIN_Y, PIN_G]

GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_Y, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)

print("LED ready")

while True:
   for pin in PIN_ALL:
       GPIO.output(pin, GPIO.HIGH)
       time.sleep(1)

   for pin in PIN_ALL:
       GPIO.output(pin, GPIO.LOW)
       time.sleep(1)




