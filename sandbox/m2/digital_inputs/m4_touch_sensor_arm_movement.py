# !/usr/bin/env python3
"""
In this module you will use the touch sensor to make arm movements.  Instead of writing code from scratch you will
fix the existing code, which is FULL of bugs.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

MAX_SPEED = 900

# TODO: 2. Have someone on your team run this program as is on the EV3 and make sure everyone understands the code.
# Can you see what the robot does and explain what each line of code is doing? Talk as a group to make sure.


def main():
    print("--------------------------------------------")
    print(" Touch sensor arm movements")
    print("--------------------------------------------")
    ev3.Sound.speak("Touch sensor arm movements").wait()

    arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
    assert arm_motor.connected

    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    while True:
        command_to_run = input("Enter c (for calibrate), u (for up), d (for down), or q (for quit): ")
        if command_to_run == 'c':
            print("Calibrate the arm")
            print("TODO: 3 is to delete this print statement, uncomment the line below, and implement that function.")
            # arm_calibration(arm_motor, touch_sensor)
        elif command_to_run == 'u':
            print("Move the arm to the up position")
            print("TODO: 4 is to delete this print statement, uncomment the line below, and implement that function.")
            # arm_up(arm_motor, touch_sensor)
        elif command_to_run == 'd':
            print("Move the arm to the down position")
            print("TODO: 5 is to delete this print statement, uncomment the line below, and implement that function.")
            # arm_down(arm_motor)
        elif command_to_run == 'q':
            break
        else:
            print(command_to_run, "is not a known command. Please enter a valid choice.")

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


def arm_calibration(arm_motor, touch_sensor):
    """
    Runs the arm up until the touch sensor is hit then back to the bottom again, beeping at both locations.
    Once back at in the bottom position, gripper open, set the absolute encoder position to 0.  You are calibrated!
    The Snatch3r arm needs to move 14.2 revolutions to travel from the touch sensor to the open position.

    Type hints:
      :type arm_motor: ev3.MediumMotor
      :type touch_sensor: ev3.TouchSensor
    """
    # TODO: 3. Implement the arm calibration movement by fixing the code below (it has many bugs).  It should to this:
    #   Command the arm_motor to run forever in the positive direction at max speed.
    #   Create an infinite while loop that will block code execution until the touch sensor's is_pressed value is True.
    #     Within that loop sleep for 0.01 to avoid running code too fast.
    #   Once past the loop the touch sensor must be pressed. So stop the arm motor quickly using the brake stop action.
    #   Make a beep sound
    #   Now move the arm_motor 14.2 revolutions in the negative direction relative to the current location
    #     Note the stop action and speed are already set correctly so we don't need to specify them again
    #   Block code execution by waiting for the arm to finish running
    #   Make a beep sound
    #   Set the arm encoder position to 0 (the last line below is correct to do that, it's new so no bug there)

    # Code that attempts to do this task but has MANY bugs (nearly 1 on every line).  Fix them!
    arm_motor.run_forever(speed_sp=100)
    while not touch_sensor:
        time.sleep(0.01)
    arm_motor.stop(stop_action="coast")

    arm_revolutions_for_full_range = 14.2
    arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range)
    arm_motor.wait_while(ev3.Motor.STATE_STALLED)

    arm_motor.position = 0  # Calibrate the down position as 0 (this line is correct as is).


def arm_up(arm_motor, touch_sensor):
    """
    Moves the Snatch3r arm to the up position.

    Type hints:
      :type arm_motor: ev3.MediumMotor
      :type touch_sensor: ev3.TouchSensor
    """
    # TODO: 4. Implement the arm up movement by fixing the code below
    # Command the arm_motor to run forever in the positive direction at max speed.
    # Create a while loop that will block code execution until the touch sensor is pressed.
    #   Within the loop sleep for 0.01 to avoid running code too fast.
    # Once past the loop the touch sensor must be pressed. Stop the arm motor using the brake stop action.
    # Make a beep sound

    # Code that attempts to do this task but has many bugs.  Fix them!
    arm_motor.run_to_rel_pos(position_sp=14.2, speed_sp=MAX_SPEED)
    while touch_sensor.is_pressed:
        time.sleep(0.01)
    arm_motor.stop()


def arm_down(arm_motor):
    """
    Moves the Snatch3r arm to the down position.

    Type hints:
      :type arm_motor: ev3.MediumMotor
    """
    # TODO: 5. Implement the arm up movement by fixing the code below
    # Move the arm to the absolute position_sp of 0 at max speed.
    # Wait until the move completes
    # Make a beep sound

    # Code that attempts to do this task but has bugs.  Fix them.
    arm_motor.run_to_abs_pos()
    arm_motor.wait_while(ev3.Motor.STATE_HOLDING)  # Blocks until the motor finishes running

    # TODO: 6. After you fix the bugs in the three arm movement commands demo your code to a TA or instructor.
    #
    # Observations you should make, the TouchSensor is easy to use, but the motor commands are still a little bit
    #   tricky.  It is neat that the same motor API works for both the wheels and the arm.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
