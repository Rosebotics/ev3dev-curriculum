#!/usr/bin/env python3
"""
The goal of this module is to let you practice with monitoring distance with the IR sensor.
You will use the IR Sensor's proximity property to beep when a hand is placed in front of the robot.

If the proximity is less than 10 then beep.  After a beep time.sleep(1.5) to allow them to remove their hand.
Check every 0.1 seconds for a hand and print the proximity value each check.

Setup the program to continue to run until the user presses the touch sensor.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Beep at hands")
    print("--------------------------------------------")
    ev3.Sound.speak("Beep at hands")

    robot = robo.Snatch3r()

    while not robot.touch_sensor.is_pressed:
        # TODO: 2. Implement the module as described in the opening comment block.
        # It is recommended that you add to your Snatch3r class's constructor the ir_sensor, as shown
        #   self.ir_sensor = ev3.InfraredSensor()
        #   assert self.ir_sensor
        # Then here you can use a command like robot.ir_sensor.proximity
        current_proximity = robot.ir_sensor.proximity
        print("Proximity: ", current_proximity)
        if current_proximity < 10:
            ev3.Sound.beep().wait()
            time.sleep(1.5)
        time.sleep(0.1)

    robot.shutdown()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
