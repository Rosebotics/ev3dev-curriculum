#!/usr/bin/env python3
"""

Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Print Pixy readings")
    print(" Press the touch sensor to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("Print Pixy readings").wait()

    pixy = ev3.Sensor(driver_name="pixy-lego")
    assert pixy.connected

    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    pixy.mode = "SIG1"

    while not touch_sensor.is_pressed:
        print("(X, Y) = ({}, {})    Width = {} Height = {}".format(
            pixy.value(1), pixy.value(2), pixy.value(3), pixy.value(4)))
        time.sleep(0.5)

    ev3.Sound.speak("Goodbye")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

