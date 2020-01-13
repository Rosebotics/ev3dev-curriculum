#!/usr/bin/env python3
"""
This module lets you practice using the encoder to determine distances while blocking code execution until complete.

You will now use a run_to_rel_pos command to implement the action drive inches action.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  January 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Copy the contents of your m1_drive_timed.py and paste that text into this file below these comments.
# TODO: 3. Add a beep after the drive motors stop (see code below).  Test your code to hear the beep AFTER movement.
#   ev3.Sound.beep().wait()
# TODO: 4. Instead of using the run_forever, time.sleep, stop pattern switch to using the run_to_rel_pos command.
#   You will need to determine the position_sp value for the command.  Assume the diameter of the wheel is ~1.3"
#   Math hints, a 1.3" diameter results in approximately a 4" circumference, so 360 degrees = 4 inches of travel
#   So you need to move through 90 degrees for every inch of travel. That value is very handy!
# TODO: 5. Make sure the beep happens after the motors stop.  Use the wait_while command to block code execution.
# TODO: 7. Formally test your work. When you think you have the problem complete run these tests:
# 200 dps 24 inches (make sure it drives within 2 inches of the target distance)
# 400 dps 24 inches (make sure it drives within 2 inches of the target distance)
# 800 dps 24 inches (make sure it drives within 2 inches of the target distance)
# 400 dps 12 inches (make sure it drives within 1 inches of the target distance)
# 400 dps 36 inches (make sure it drives within 3 inches of the target distance)
# Add more tests as you see fit.  Ideally you should be +/- 10% of the target goal this time.
#
# Observations you should make, run_to_rel_pos is easier to use since it uses encoders that are independent of speed.

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Drive using encoder")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive using encoder").wait()

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    while True:
        speed_deg_per_second = int(input("What speed would you like to go (0 to 900)? "))
        if speed_deg_per_second == 0:
            break
        inches_target = int(input("How many inches would you like to travel (0 to exit)? "))
        if inches_target == 0:
            break

        degrees_per_inch = 90
        motor_turns_deg = inches_target * degrees_per_inch

        left_motor.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=speed_deg_per_second, stop_action="brake")
        right_motor.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=speed_deg_per_second, stop_action="brake")
        time.sleep(0.1)
        left_motor.wait_while("running")  # Wait for the turn to finish
        right_motor.wait_while("running")  # Wait for the turn to finish
        ev3.Sound.beep().wait()  # Fun little beep

    ev3.Sound.speak("Goodbye").wait()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
