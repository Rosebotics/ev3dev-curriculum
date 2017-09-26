#!/usr/bin/env python3
"""
The goal of this module is to let you practice with driving and color sensing.  You need to
have a few color squares placed in a line in front of the robot.  The robot should drive over
the color squares and stop at the appropriate color (ignoring incorrect colors until the target
color is found).

Here is a link to a Google doc that has color squares that you can print (in color)
https://docs.google.com/document/d/1ed_vWTfOu15ziF8nfZwhjrRcSufKODhQtAmY8lsGNAc/edit?usp=sharing

If the user presses the Up    button, the robot drives until the robot gets to Red.
If the user presses the Down  button, the robot drives until the robot gets to Blue.
If the user presses the Left  button, the robot drives until the robot gets to Black.
If the user presses the Right button, the robot drives until the robot gets to White.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


# Potential values of the color_sensor.color property
#   ev3.ColorSensor.COLOR_NOCOLOR is the value 0
#   ev3.ColorSensor.COLOR_BLACK   is the value 1
#   ev3.ColorSensor.COLOR_BLUE    is the value 2
#   ev3.ColorSensor.COLOR_GREEN   is the value 3
#   ev3.ColorSensor.COLOR_YELLOW  is the value 4
#   ev3.ColorSensor.COLOR_RED     is the value 5
#   ev3.ColorSensor.COLOR_WHITE   is the value 6
#   ev3.ColorSensor.COLOR_BROWN   is the value 7
COLOR_NAMES = ["None", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
# This list is just a helper list if you ever want the string (for printing or speaking) from a color value.


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")
    print(" Drive to the color")
    print("  Up button goes to Red")
    print("  Down button goes to Blue")
    print("  Left button goes to Black")
    print("  Right button goes to White")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive to the color").wait()
    print("Press Back to exit this program.")

    robot = robo.Snatch3r()
    dc = DataContainer()

    # For our standard shutdown button.
    btn = ev3.Button()
    # TODO: 2. Uncomment the lines below to setup event handlers for these buttons.
    # btn.on_up = lambda state: drive_to_color(state, robot, ev3.ColorSensor.COLOR_RED)
    # btn.on_down = lambda state: drive_to_color(state, robot, ev3.ColorSensor.COLOR_BLUE)
    # btn.on_left = lambda state: drive_to_color(state, robot, ev3.ColorSensor.COLOR_BLACK)
    # btn.on_right = lambda state: drive_to_color(state, robot, ev3.ColorSensor.COLOR_WHITE)
    btn.on_backspace = lambda state: handle_shutdown(state, dc)

    while dc.running:
        btn.process()
        time.sleep(0.01)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Event handlers
# ----------------------------------------------------------------------
def drive_to_color(button_state, robot, color_to_seek):
    """
    When the button_state is True (pressed), drives the robot forward until the desired color is detected.
    When the color_to_seek is detected the robot stops moving forward and speaks a message.

    Type hints:
      :type button_state: bool
      :type robot: robo.Snatch3r
      :type color_to_seek: int
    """
    if button_state:
        ev3.Sound.speak("Seeking " + COLOR_NAMES[color_to_seek]).wait()

        # TODO: 3. Implement the task as stated in this module's initial comment block
        # It is recommended that you add to your Snatch3r class's constructor the color_sensor, as shown
        #   self.color_sensor = ev3.ColorSensor()
        #   assert self.color_sensor
        # Then here you can use a command like robot.color_sensor.color to check the value



        # TODO: 4. Call over a TA or instructor to sign your team's checkoff sheet.
        #
        # Observations you should make, the instance variable robot.color_sensor.color is always updating
        # to the color seen and that value is given to you as an int.

        ev3.Sound.speak("Found " + COLOR_NAMES[color_to_seek]).wait()


def handle_shutdown(button_state, dc):
    """Exit the program."""
    if button_state:
        dc.running = False


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
