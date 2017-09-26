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
    print("Press the touch sensor to exit this program.")

    robot = robo.Snatch3r()
    # Note, it is assumed that you have a touch_sensor property on the Snatch3r class.
    # Presumably you added this in the digital_inputs unit, if not add it now so that
    # the code below works to monitor the touch_sensor.

    while not robot.touch_sensor.is_pressed:
        # TODO: 2. Implement the module as described in the opening comment block.
        # It is recommended that you add to your Snatch3r class's constructor the ir_sensor, as shown
        #   self.ir_sensor = ev3.InfraredSensor()
        #   assert self.ir_sensor
        # Then here you can use a command like robot.ir_sensor.proximity

        time.sleep(0.1)

    # TODO: 3. Call over a TA or instructor to sign your team's checkoff sheet.
    #
    # Observations you should make, the instance variable robot.ir_sensor.proximity is always updating with a distance.

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
