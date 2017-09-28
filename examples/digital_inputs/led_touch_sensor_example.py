#!/usr/bin/env python3
"""
Example of using LED syntax and the Touch Sensor.  Also a fun little robot countdown.

Author: David Fisher.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print("    Touch Sensor + LEDs")
    print("--------------------------------------------")
    ev3.Sound.speak("Touch sensor L E Dees").wait()

    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    for k in range(100):
        time.sleep(0.1)
        if touch_sensor.is_pressed:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.ORANGE)
        else:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)
        if k % 10 == 0:
            ev3.Sound.speak(10 - (k // 10)).wait()

    ev3.Leds.all_off()

    print("Goodbye")
    ev3.Sound.speak("Goodbye").wait()
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
