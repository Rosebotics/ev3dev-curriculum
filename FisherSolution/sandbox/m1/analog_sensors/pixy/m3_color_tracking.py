#!/usr/bin/env python3
"""
The goal of this module to combine using the Pixy with the drive motors.  You will track a color using the Pixy and turn
the robot so that it is always facing the color signature.  You will need to teach Pixy a color before starting to
implement the code, then make the robot always face the color as you move it around.  The robot will only spin and never
move forwards or backwards.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Color tracking")
    print(" Press the touch sensor to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("Color tracking").wait()

    robot = robo.Snatch3r()
    robot.pixy.mode = "SIG1"
    turn_speed = 100

    while not robot.touch_sensor.is_pressed:

        # TODO: 3. Read the Pixy values for x and y
        # Print the values for x and y

        # TODO: 4. Use the x value to turn the robot
        #   If the Pixy x value is less than 150 turn left (-turn_speed, turn_speed)
        #   If the Pixy x value is greater than 170 turn right (turn_speed, -turn_speed)
        #   If the Pixy x value is between 150 and 170 stop the robot
        # Continuously track the color until the touch sensor is pressed to end the program.

        x = robot.pixy.value(1)
        y = robot.pixy.value(2)
        print("(X, Y) = ({}, {})".format(x, y))

        if x < 150:
            robot.drive(-turn_speed, turn_speed)
        elif x > 170:
            robot.drive(turn_speed, -turn_speed)
        else:
            robot.stop()

        time.sleep(0.25)

    robot.shutdown()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

