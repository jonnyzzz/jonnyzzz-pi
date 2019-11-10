#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

PIN_IR = 18

GPIO.setup(PIN_IR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("IR ready, reading...")


def handle_ir_packet(channel):
    print("Signal is detected!")
    

GPIO.add_event_detect(PIN_IR, GPIO.FALLING, callback=handle_ir_packet, bouncetime=300)

input("Press key to stop")
GPIO.cleanup()


#while True:
#    print("Waiting for the signal...")
#
#
#    GPIO.wait_for_edge(PIN_IR, GPIO.FALLING)
#    print("Signal is detected!")
#    time.sleep(0.2)




#    v = GPIO.input(PIN_IR)



#    print("IR - %d\n" % v)
#    time.sleep(0.005) ##  5ms


   



