#!/usr/bin/env python3
"""
This module is an example of using the Lego Pixy camera.  It prints the x, y, width, and height
of color signature 1.  Before you use this program, make sure you have setup the Pixy to track
a color signature.

Authors: David Fisher.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Print Pixy readings")
    print("--------------------------------------------")
    ev3.Sound.speak("Print Pixy readings").wait()
    print(" Press the touch sensor to exit")

    pixy = ev3.Sensor(driver_name="pixy-lego")
    assert pixy.connected

    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    pixy.mode = "SIG1"

    while not touch_sensor.is_pressed:
        print("(X, Y) = ({}, {})    Width = {} Height = {}".format(
            pixy.value(1), pixy.value(2), pixy.value(3), pixy.value(4)))
        time.sleep(0.5)

    print("Goodbye")
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

