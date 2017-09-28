#!/usr/bin/env python3
"""
Drives the EV3 in a square (the accuracy of the 90 degree turns will vary by surface type).
Demo video: https://goo.gl/photos/vrrSnLUvx8mSGCvZ6

Author: David Fisher.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print("  Drive square")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive square").wait()

    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    # Displays a list of commands for a motor
    print("Motor commands:", left_motor.commands)

    # Drive in a square
    edge_length_drive_time_s = 6.0
    for _ in range(4):
        drive_straight(left_motor, right_motor, edge_length_drive_time_s)
        turn_90(left_motor, right_motor)
        time.sleep(0.5)
    shutdown(left_motor, right_motor)


def drive_straight(left_motor, right_motor, time_s):
    """
    Shows an example of using run_forever at a given speed.

    Type hints:
      :type left_motor: ev3.Motor
      :type right_motor: ev3.Motor
      :type time_s: int | float
    """
    print("Driving straight...")
    left_motor.run_forever(speed_sp=400)
    right_motor.run_forever(speed_sp=400)
    time.sleep(time_s)
    left_motor.stop(stop_action="brake")
    right_motor.stop(stop_action="brake")
    # This solution uses run_forever then a time delay there is also a run_timed method
    # that could've been used instead if control needs to be returned immediately
    # Typically the solution above is the more common drive pattern.


def turn_90(left_motor, right_motor):
    """
    Shows an example of using run_to_rel_pos at a given speed.

    Type hints:
      :type left_motor: ev3.Motor
      :type right_motor: ev3.Motor
    """
    print("Turning...")
    motor_turns_deg = 486  # May require some tuning depending on your surface!
    left_motor.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=400)
    right_motor.run_to_rel_pos(position_sp=-motor_turns_deg, speed_sp=400)
    # Note, that there is no delay using the commands above, so we must wait
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Wait for the turn to finish
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Wait for the turn to finish
    ev3.Sound.beep().wait()  # Fun little beep


def drive(left_motor, right_motor, left_sp, right_sp):
    """
    Drive the robot forward at the given speeds.

    Type hints:
      :type left_motor: ev3.Motor
      :type right_motor: ev3.Motor
      :type left_sp: int
      :type right_sp: int
    """
    left_motor.run_forever(speed_sp=left_sp)
    right_motor.run_forever(speed_sp=right_sp)


def shutdown(left_motor, right_motor):
    """
    Close the program

    Type hints:
      :type left_motor: ev3.Motor
      :type right_motor: ev3.Motor
    """
    print("Goodbye!")
    left_motor.stop(stop_action="coast")
    right_motor.stop(stop_action="coast")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    ev3.Sound.speak("Goodbye").wait()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
