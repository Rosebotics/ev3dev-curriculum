#!/usr/bin/env python3
"""
The goal of this example is to show you the syntax for IR distance readings.  Additionally
it's good to play with a demo so that you can see how well or not well a sensor behaves.
To test this module run it, place the IR Sensor at 0 cm on your ruler, then hold a white
sheet of paper some distance away.  Watch the values print as you move the paper closer and
farther away.  How well do the values match the number of centimeters away?

Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Printing distances")
    print(" Press the touch sensor to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("Printing distance").wait()

    touch_sensor = ev3.TouchSensor()
    ir_sensor = ev3.InfraredSensor()
    assert touch_sensor
    assert ir_sensor

    while not touch_sensor.is_pressed:
        current_proximity = ir_sensor.proximity
        print("IR Distance = {}".format(current_proximity))
        time.sleep(0.5)

    ev3.Sound.speak("Goodbye")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
