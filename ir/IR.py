#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

PIN_IR = 18

GPIO.setup(PIN_IR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("IR ready, reading...")
print("time_ns == ", time.time_ns())

def time_mks():
    return time.monotonic_ns() // 1000

def handle_ir_packet(channel):
    vs = [ 0 ]
    times = [ 0 ]

    start_time = time_mks()
    while True:
        now = time_mks() - start_time
        if now > 300000: 
            break

        times.append(now)
        vs.append(GPIO.input(channel))
        time.sleep(200.0 / 1000.0 / 1000.0) # avg 200ms

    print("data:", " ".join(map(str, vs)))
    print("times:", " ".join(map(str, times)))

handle_ir_packet(PIN_IR)

GPIO.add_event_detect(PIN_IR, GPIO.FALLING, callback=handle_ir_packet, bouncetime=300)

input("Press key to stop...\n")
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


   



