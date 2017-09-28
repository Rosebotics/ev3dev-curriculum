#!/usr/bin/env python3
"""
This module prints messages when buttons on the IR remote or the EV3 primary buttons are pressed and released.
Copying the boilerplate code can save you a lot of typing if using buttons in your own projects.

Author: David Fisher.
"""

import ev3dev.ev3 as ev3
import time


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")
    print("   Example of buttons with event handlers")
    print("--------------------------------------------")
    ev3.Sound.speak("Buttons with events").wait()

    robot = None  # Requires you to implement the Snatch3r class in the robot_controller library
    dc = DataContainer()  # Optional class to help you pass around data between different button events.

    # Remote control channel 1
    rc1 = ev3.RemoteControl(channel=1)
    assert rc1.connected
    rc1.on_red_up = lambda state: handle_red_up_1(state, robot, dc)
    rc1.on_red_down = lambda state: handle_red_down_1(state, robot, dc)
    rc1.on_blue_up = lambda state: handle_blue_up_1(state, robot, dc)
    rc1.on_blue_down = lambda state: handle_blue_down_1(state, robot, dc)

    # Remote control channel 2
    rc2 = ev3.RemoteControl(channel=2)
    assert rc2.connected
    rc2.on_red_up = lambda state: handle_red_up_2(state, robot, dc)
    rc2.on_red_down = lambda state: handle_red_down_2(state, robot, dc)
    rc2.on_blue_up = lambda state: handle_blue_up_2(state, robot, dc)
    rc2.on_blue_down = lambda state: handle_blue_down_2(state, robot, dc)

    # Buttons on EV3
    btn = ev3.Button()
    btn.on_up = lambda state: handle_up_button(state, robot, dc)
    btn.on_down = lambda state: handle_down_button(state, robot, dc)
    btn.on_left = lambda state: handle_left_button(state, robot, dc)
    btn.on_right = lambda state: handle_right_button(state, robot, dc)
    # Note there is also an enter button but sometimes that causes issues with Brickman when used
    btn.on_backspace = lambda state: handle_shutdown(state, robot, dc)

    while dc.running:
        rc1.process()
        rc2.process()
        btn.process()
        time.sleep(0.01)


# ----------------------------------------------------------------------
# Event handlers
# Remote Control channel 1
# ----------------------------------------------------------------------
def handle_red_up_1(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Red up channel 1 is pressed")
    else:
        print("Red up channel 1 was released")


def handle_red_down_1(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Red down channel 1 is pressed")
    else:
        print("Red down channel 1 was released")


def handle_blue_up_1(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Blue up channel 1 is pressed")
    else:
        print("Blue up channel 1 was released")


def handle_blue_down_1(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Blue down channel 1 is pressed")
    else:
        print("Blue down channel 1 was released")


# ----------------------------------------------------------------------
# Remote Control channel 2
# ----------------------------------------------------------------------
def handle_red_up_2(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Red up channel 2 is pressed")
    else:
        print("Red up channel 2 was released")


def handle_red_down_2(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Red down channel 2 is pressed")
    else:
        print("Red down channel 2 was released")


def handle_blue_up_2(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Blue up channel 2 is pressed")
    else:
        print("Blue up channel 2 was released")


def handle_blue_down_2(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Blue down channel 2 is pressed")
    else:
        print("Blue down channel 2 was released")


# ----------------------------------------------------------------------
# Buttons
# ----------------------------------------------------------------------
def handle_up_button(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Up button is pressed")
    else:
        print("Up button was released")


def handle_down_button(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Down button is pressed")
    else:
        print("Down button was released")


def handle_left_button(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Left button is pressed")
    else:
        print("Left button was released")


def handle_right_button(button_state, robot, dc):
    """
    Handle IR / button event.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        print("Right button is pressed")
    else:
        print("Right button was released")


def handle_shutdown(button_state, robot, dc):
    """
    Exit the program using the robot shutdown command.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type dc: DataContainer
    """
    if button_state:
        # robot.shutdown()  # To stop motors and turn on the GREEN leds.
        dc.running = False


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
