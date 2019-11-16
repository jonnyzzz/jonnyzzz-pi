#!/usr/bin/python3

import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_R = 16
PIN_Y = 21
PIN_G = 20

PIN_A = 25
PIN_B = 8
PIN_C = 7
PIN_D = 12

PIN_ALL = [PIN_R, PIN_Y, PIN_G]
PORTS = [PIN_A, PIN_B, PIN_C, PIN_D]

# configure ports
for p in PIN_ALL + PORTS:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.HIGH)


class TrafficLight:
    def __init__(self, pin, light):
        self.pin = pin
        self.light = light
        self.p_red = {k: GPIO.HIGH if k == PIN_R else GPIO.LOW for k in PIN_ALL}
        self.p_red_yellow = {k: GPIO.HIGH if k != PIN_G else GPIO.LOW for k in PIN_ALL}
        self.p_yellow = {k: GPIO.HIGH if k == PIN_Y else GPIO.LOW for k in PIN_ALL}
        self.p_green = {k: GPIO.HIGH if k == PIN_G else GPIO.LOW for k in PIN_ALL}
        self.p_dark = {k: GPIO.LOW for k in PIN_ALL}

    def dark(self):
        self.light.update(self.p_dark)

    def red(self):
        self.light.update(self.p_red)

    def red_yellow(self):
        self.light.update(self.p_red_yellow)

    def yellow(self):
        self.light.update(self.p_yellow)

    def green(self):
        self.light.update(self.p_green)

    def start(self):
        def thread_run():
            print("Starting LED for %d!" % self.pin)

            long = 3
            short = long / 8

            while True:
                self.red()
                time.sleep(long)
                self.red_yellow()
                time.sleep(short)
                self.green()
                time.sleep(long)

                for _ in [1, 2, 3]:
                    self.yellow()
                    time.sleep(short)
                    self.dark()
                    time.sleep(short)

        thread = threading.Thread(target=thread_run)
        thread.start()


class LEDThread:
    def __init__(self):
        # pin -> light -> state
        self.lights = {k: {p: GPIO.HIGH for p in PIN_ALL} for k in PORTS}

    def all_lights(self):
        return [TrafficLight(k, v) for k, v in self.lights.items()]

    def run(self):
        print("Starting LED thread!")

        def active_ports_iterator():
            for p in PORTS:
                GPIO.output(p, GPIO.LOW)

            prev = PORTS[0]
            while True:
                for p in PORTS:
                    GPIO.output(prev, GPIO.LOW)
                    GPIO.output(p, GPIO.HIGH)
                    prev = p
                    yield p

        for p in active_ports_iterator():
            light = self.lights[p]
            for k, v in light.items():
                GPIO.output(k, v)

    def start(self):
        def thread_run():
            self.run()

        thread = threading.Thread(target=thread_run)
        thread.start()


LED = LEDThread()

for q in LED.all_lights():
    q.start()
    time.sleep(0.7)

LED.start()
time.sleep(9939393945)
