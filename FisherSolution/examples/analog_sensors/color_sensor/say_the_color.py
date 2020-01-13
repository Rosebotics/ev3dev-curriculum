#!/usr/bin/env python3
"""
This module will speak the name of the color that the color sensor sees.  Place a color
under the color sensor to see if the name is spoken that you expect.

This demo shows you the code to use the color_sensor.color property.  To be honest, it's
pretty easy to use. So the other value of this demo is to test your color squares.  It's
surprisingly hard sometimes to print something say yellow and have the robot not call it
blue. :)  Red, Blue, Black, and White are rock solid, but Green, Yellow, and Brown are
well... worth testing.

Authors: David Fisher.  February 2017.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Say the Color")
    print(" Press the touch sensor to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("Say the Color").wait()

    color_sensor = ev3.ColorSensor()
    assert color_sensor

    # Potential values of the color_sensor.color property
    # 0: No color
    # 1: Black
    # 2: Blue
    # 3: Green
    # 4: Yellow
    # 5: Red
    # 6: White
    # 7: Brown
    # From http://python-ev3dev.readthedocs.io/en/latest/sensors.html#special-sensor-classes

    last_color_spoken = 0  # No color name has been spoken.

    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    while not touch_sensor.is_pressed:
        current_color = color_sensor.color
        if current_color == 0:
            last_color_spoken = current_color  # Clear the saved value
        else:
            if current_color != last_color_spoken:
                last_color_spoken = current_color  # Avoid saying the name again immediately.
                if current_color == 1:
                    ev3.Sound.speak("Black").wait()
                elif current_color == 2:
                    ev3.Sound.speak("Blue").wait()
                elif current_color == 3:
                    ev3.Sound.speak("Green").wait()
                elif current_color == 4:
                    ev3.Sound.speak("Yellow").wait()
                elif current_color == 5:
                    ev3.Sound.speak("Red").wait()
                elif current_color == 6:
                    ev3.Sound.speak("White").wait()
                elif current_color == 7:
                    ev3.Sound.speak("Brown").wait()

        # Hit Ctrl-c to exit as there is no other way out!
        time.sleep(0.05)

    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
