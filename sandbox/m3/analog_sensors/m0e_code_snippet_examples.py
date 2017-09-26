#!/usr/bin/env python3
"""
Contains example code snippets used in the drive motor lecture.  Don't try to actually run this file!
These are just snippets used in the lecture, not actual code to run!

TODO: 1. PASSIVELY LISTEN TO THE LECTURE ABOUT ANALOG SENSORS
https://docs.google.com/presentation/d/1U00IlFqIT_S2v9HV-TKSO6Y6foH4sDom9yytsV_PWfY/edit?usp=sharing

Author: David Fisher
"""

import ev3dev.ev3 as ev3
import time


def color_sensor_color():
    """ Example of detecting color with the color sensor. """
    color_sensor = ev3.ColorSensor()

    # Potential values of the color_sensor.color property
    #   ev3.ColorSensor.COLOR_NOCOLOR is the value 0
    #   ev3.ColorSensor.COLOR_BLACK   is the value 1
    #   ev3.ColorSensor.COLOR_BLUE    is the value 2
    #   ev3.ColorSensor.COLOR_GREEN   is the value 3
    #   ev3.ColorSensor.COLOR_YELLOW  is the value 4
    #   ev3.ColorSensor.COLOR_RED     is the value 5
    #   ev3.ColorSensor.COLOR_WHITE   is the value 6
    #   ev3.ColorSensor.COLOR_BROWN   is the value 7
    # From http://python-ev3dev.readthedocs.io/en/latest/sensors.html#special-sensor-classes

    for _ in range(5):
        current_color = color_sensor.color
        if current_color == ev3.ColorSensor.COLOR_RED:
            ev3.Sound.speak("I see Red").wait()
        else:
            color_names = ["No color", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
            print("I see " + color_names[current_color])
        time.sleep(1.0)


def color_sensor_reflected_light_intensity():
    """ Example of detecting how much light is reflected to the color sensor. """
    color_sensor = ev3.ColorSensor()

    # Potential values of the color_sensor.reflected_light_intensity property
    # 0       (0% light reflected) nothing was reflected, you are in a perfect cave
    # 1 to 99 (1% to 99% light reflected) real readings will be somewhere in this range
    # 100     (100% light reflected) perfect reflecting object (white) at close range

    for _ in range(5):
        percent_reflected = color_sensor.reflected_light_intensity
        print("The amount of light reflected is {}%.".format(percent_reflected))
        time.sleep(1.0)


def ir_sensor_proximity():
    """ Example of using the IR sensor as a distance measuring device or as an IR-SEEK sensor. """
    ir_sensor = ev3.InfraredSensor()

    # Potential values of the ir_sensor.proximity property
    # 0       (Object is 0% away) something is super close (sensor does not work well this close)
    # 1 to 99 (Object is 1% to 99% away) real readings will be somewhere in this range
    # 100     (Object is 100% away) nothing in front of the sensor

    print(ir_sensor.proximity)  # To measure distance to a wall

    # To find the IR beacon (with the remote in beacon mode)
    beacon_seeker = ev3.BeaconSeeker()  # Assumes remote is set to channel 1
    print("Heading", beacon_seeker.heading)
    print("Distance", beacon_seeker.distance)


def pixy_example():
    """ Example of using the Pixy to print the x, y, width, and height of color signature 1. """
    pixy = ev3.Sensor(driver_name="pixy-lego")

    pixy.mode = "SIG1"
    print("value0: Count", pixy.value(0))  # Probably not useful
    print("value1: X", pixy.value(1))
    print("value2: Y", pixy.value(2))
    print("value3: Width", pixy.value(3))
    print("value4: Height", pixy.value(4))
