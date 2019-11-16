#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

PIN_R = 16
PIN_Y = 21
PIN_G = 20

PIN_A = 25
PIN_B = 8
PIN_C = 7
PIN_D = 12

PIN_ALL = [PIN_R, PIN_Y, PIN_G]

GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_Y, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)

GPIO.setup(PIN_A, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)
GPIO.setup(PIN_C, GPIO.OUT)
GPIO.setup(PIN_D, GPIO.OUT)

GPIO.output(PIN_A, GPIO.HIGH)
GPIO.output(PIN_B, GPIO.HIGH)
GPIO.output(PIN_C, GPIO.HIGH)
GPIO.output(PIN_D, GPIO.HIGH)

GPIO.output(PIN_R, GPIO.HIGH)
GPIO.output(PIN_Y, GPIO.HIGH)
GPIO.output(PIN_G, GPIO.HIGH)

# time.sleep(900009)
print("LED ready!")

long = 3
short = long / 8

def red():
    GPIO.output(PIN_R, GPIO.HIGH)
    GPIO.output(PIN_Y, GPIO.LOW)
    GPIO.output(PIN_G, GPIO.LOW)
    time.sleep(long)


def red_yellow():
    GPIO.output(PIN_R, GPIO.HIGH)
    GPIO.output(PIN_Y, GPIO.HIGH)
    GPIO.output(PIN_G, GPIO.LOW)
    time.sleep(long)


def yellow():
    GPIO.output(PIN_R, GPIO.LOW)
    GPIO.output(PIN_Y, GPIO.HIGH)
    GPIO.output(PIN_G, GPIO.LOW)
    time.sleep(short)


def dark():
    GPIO.output(PIN_R, GPIO.LOW)
    GPIO.output(PIN_Y, GPIO.LOW)
    GPIO.output(PIN_G, GPIO.LOW)
    time.sleep(short)


def green():
    GPIO.output(PIN_R, GPIO.LOW)
    GPIO.output(PIN_Y, GPIO.LOW)
    GPIO.output(PIN_G, GPIO.HIGH)
    time.sleep(long)


while True:
    red()
    red_yellow()
    green()

    for _ in [1, 2, 3]:
        yellow()
        dark()






