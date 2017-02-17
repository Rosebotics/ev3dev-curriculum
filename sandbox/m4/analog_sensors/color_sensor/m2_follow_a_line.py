# !/usr/bin/env python3
"""
In this module you will practice using the reflected_light_intensity property of the color
sensor.  This module uses a simple input to:

w - Calibrate the white value. Put the robot on white and determine what value is a white surface.
b - Calibrate the black value. Put the robot on black and determine what value is a black surface.
f - Follow the line until the touch sensor is pressed.  You are allowed to assume in your code
     that the line only ever goes straight or turns to the right.
     Extra - For a harder challenge could you drive on the black line and handle left or right turns?
q - Quit

Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Follow a line")
    print("--------------------------------------------")
    ev3.Sound.speak("Follow a line").wait()

    # TODO: 4: After running the code set the default white and black levels to a better initial guess.
    white_level = 50
    black_level = 40
    robot = robo.Snatch3r()

    while True:
        command_to_run = input("Enter w (white), b (black), f (follow), or q (for quit): ")
        if command_to_run == 'w':
            print("Calibrate the white light level")
            # TODO: 2. Read the reflected_light_intensity property of the color sensor and set white_level
            # As discussed in the prior module, it is recommended that you've added to your Snatch3r class's constructor
            # the color_sensor, as shown:
            #   self.color_sensor = ev3.ColorSensor()
            #   assert self.color_sensor
            # Then here you can use a command like robot.color_sensor.reflected_light_intensity


            print("New white level is {}.".format(white_level))
        elif command_to_run == 'b':
            print("Calibrate the black light level")
            # TODO: 3. Read the reflected_light_intensity property of the color sensor and set black_level


            print("New black level is {}.".format(black_level))
        elif command_to_run == 'f':
            print("Follow the line until the touch sensor is pressed.")
            follow_the_line(robot, white_level, black_level)
        elif command_to_run == 'q':
            break
        else:
            print(command_to_run, "is not a known command. Please enter a valid choice.")

    ev3.Sound.speak("Goodbye").wait()


def follow_the_line(robot, white_level, black_level):
    """ The robot follows the black line until the touch sensor is pressed.
        When the touch sensor is pressed, line following ends and control is returned to main."""

    # TODO: 5. Use the calibrated values for white and black to determine what speeds to drive to
    # follow a line.  You can drive on the black or on the white next to the black line.  You
    # can assume that the line only ever goes straight or turns right.
    # Extra - For a harder challenge could you drive on the black line and handle left or right turns?



    ev3.Sound.speak("Done")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
