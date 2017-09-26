# !/usr/bin/env python3
"""
Time to move your arm movement functions into your Snatch3r robot library.

This module will work exactly the same as the prior module but will do that work via your robot library.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Have everyone talk about this problem together then pick one team member to modify libs/robot_controller.py
# as necessary to make the code below perform the same task as the prior module. Once the code has been tested and shown
# to work, then have that person commit their work.  All other team members need to do a VCS --> Update project...
# Once the library is implemented each team member should be able to run their version of this code on the robot.

# TODO: 3. Call over a TA or instructor to sign your team's checkoff sheet and do a code review of your library.
#
# Observations you should make, you are a TEAM and making great library methods will make life easier for everyone.

import ev3dev.ev3 as ev3
import robot_controller as robo


def main():
    # --------------------------------------------------------------
    # We have already implemented this module for you.
    # There are no TODOs in the code.  Do NOT modify it.
    # You are not allowed to make any changes to this file.
    # --------------------------------------------------------------
    print("--------------------------------------------")
    print(" Arm movement via library")
    print("--------------------------------------------")
    ev3.Sound.speak("Arm movement via library").wait()
    robot = robo.Snatch3r()

    while True:
        command_to_run = input("Enter c (for calibrate), u (for up), d (for down), or q (for quit): ")
        if command_to_run == 'c':
            print("Calibrate the arm")
            robot.arm_calibration()
        elif command_to_run == 'u':
            print("Move the arm to the up position")
            robot.arm_up()
        elif command_to_run == 'd':
            print("Move the arm to the down position")
            robot.arm_down()
        elif command_to_run == 'q':
            break
        else:
            print(command_to_run, "is not a known command. Please enter a valid choice.")

    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
