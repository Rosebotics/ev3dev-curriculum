#!/usr/bin/env python3
"""
The goal of this module is to drive towards the beacon (the IR remote in beacon mode) and stop your robot right in front
of the beacon (just like the last module).  Then pick up the beacon using the gripper.  After the pickup the robot will
pause for a moment then just set the beacon back down so that you can test again.

So you need to build upon your program from the prior module and put the seek_beacon function into your Snatch3r class.

Additionally within that function we would like for you to make 2 changes:
  - If the beacon is not found due to the distance being -128, instead of stopping just spin slowly in place to find it
  - If the beacon is not found due to the heading being greater than 10, instead of stopping just spin slowly in place
Hopefully spinning slowly in place will help you find the beacon even if it starts behind you.

The code below has no TODOs, your only changes will be in the Snatch3r class.  As always, pick one person from your team
to do the typing in your class, test it together, commit the work, then have everyone Git update to get the code.

When complete call over a TA or instructor to sign your team's checkoff sheet.
You can check off this part with a single successful run (sometimes it can be hard).

Author: David Fisher.
"""
import traceback

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Beacon pickup")
    print("--------------------------------------------")
    ev3.Sound.speak("Beacon pickup").wait()

    #####################################################
    # There are no TODOs in this code.
    # Your only edits will be in the Snatch3r class.
    #####################################################

    robot = robo.Snatch3r()
    try:
        while True:
            found_beacon = robot.seek_beacon()
            if found_beacon:
                ev3.Sound.speak("I got the beacon")
                robot.arm_up()
                time.sleep(1)
                robot.arm_down()
            command = input("Hit enter to seek the beacon again or enter q to quit: ")
            if command == "q":
                break
    except:
        traceback.print_exc()
        ev3.Sound.speak("Error")

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
