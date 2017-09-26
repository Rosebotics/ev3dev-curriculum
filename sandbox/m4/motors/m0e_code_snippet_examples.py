#!/usr/bin/env python3
"""
Contains example code snippets used in the drive motor lecture.  Don't try to actually run this file!
These are just snippets used in the lecture, not actual code to run!

TODO: 1. PASSIVELY LISTEN TO THE LECTURE ABOUT DRIVE MOTORS
https://docs.google.com/presentation/d/1rjkOZNw0mO0pH7Ovhy-7riYG3Xa4xq4rKbwMPhDppJs/edit#slide=id.g2e200109_1_0

Author: David Fisher
"""

import ev3dev.ev3 as ev3
import time


def simple_drive(left_sp, right_sp, time_s):
    """ Shows the most basic drive strategy. run_forever, time.sleep, stop """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    left_motor.run_forever(speed_sp=left_sp)
    right_motor.run_forever(speed_sp=right_sp)

    time.sleep(time_s)

    left_motor.stop()
    right_motor.stop()


def motor_movement_commands():
    """Examples of each motor movement command + all parameters that make sense."""
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    left_motor.run_forever(speed_sp=-300)
    left_motor.stop(stop_action="coast")
    left_motor.run_to_abs_pos(position_sp=-360, speed_sp=400, stop_action="brake")
    left_motor.run_to_rel_pos(position_sp=720, speed_sp=400, stop_action="brake")
    left_motor.run_timed(time_sp=3000, speed_sp=400, stop_action="coast")
    # Units
    # position_sp --> degrees
    # speed_sp --> degrees per second
    # time_sp --> milliseconds


def turn_90(left_motor, right_motor):
    """Shows an example of using run_to_rel_pos at a given speed + a wait_while running."""
    motor_turns_deg = 440  # May require some tuning depending on your surface!
    left_motor.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=400)
    right_motor.run_to_rel_pos(position_sp=-motor_turns_deg, speed_sp=400)

    # Note, that there is no delay using the motor movement commands, so we must block code execution.
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Wait for the turn to finish
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Wait for the turn to finish

    ev3.Sound.beep().wait()  # Make sure beep happens AFTER the motors stop.


def using_the_concise_property_shorthand_vs_verbose():
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    # Verbose way to set properties then run a command (works fine).
    # left_motor.speed_sp = 500
    # left_motor.time_sp = 3000
    # left_motor.stop_action = "brake"
    # left_motor.run_timed()

    # Concise way to set properties then run a command (recommended).
    left_motor.run_timed(speed_sp=500, time_sp=3000, stop_action="brake")
