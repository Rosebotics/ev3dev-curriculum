# !/usr/bin/env python3
"""
In this module you will practice using the reflected_light_intensity property of the color
sensor.  This module uses a command line input to:

w - Calibrate the white value. Put the robot on white and determine what value is a white surface.
      This value will be passed into the follow_the_line function.
b - Calibrate the black value. Put the robot on black and determine what value is a black surface.
      This value will be passed into the follow_the_line function.
f - Follow the line until the touch sensor is pressed.  You are allowed to assume in your code
     that the line only ever goes straight or turns to the right (your robot will never turn left).
     Extra - For a harder challenge could you drive on the black line and handle left or right turns?
q - Quit

Authors: David Fisher and PUT_YOUR_NAME_HERE.
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
    #   Once you have the values hardcoded to resonable numbers here you don't really need the w and b commands below.
    white_level = 50
    black_level = 40
    robot = robo.Snatch3r()

    while True:
        command_to_run = input("Enter w (white), b (black), f (follow), or q (for quit): ")
        if command_to_run == 'w':
            print("Calibrate the white light level")
            # TODO: 2. Read the reflected_light_intensity property of the color sensor and set white_level to that value
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

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


def follow_the_line(robot, white_level, black_level):
    """
    The robot follows the black line until the touch sensor is pressed.
    You will need a black line track to test your code
    When the touch sensor is pressed, line following ends, the robot stops, and control is returned to main.

    Type hints:
      :type robot: robo.Snatch3r
      :type white_level: int
      :type black_level: int
    """

    # TODO: 5. Use the calibrated values for white and black to calculate a light threshold to determine if your robot
    # should drive straight or turn to the right.  You will need to test and refine your code until it works well.
    # Optional extra - For a harder challenge could you drive on the black line and handle left or right turns?

    robot.stop()
    ev3.Sound.speak("Done")


# TODO: 6. Call over a TA or instructor to sign your team's checkoff sheet and do a code review.
#
# Observations you should make, following a black line would be easier with 2 sensors (one on each side of the line),
# but it can be done with only a single sensor.  There are also optimizations that could be made to follow the line
# faster and more smoothly.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
