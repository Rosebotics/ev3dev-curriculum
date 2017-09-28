#!/usr/bin/env python3
"""
The goal of this module is to let you practice with color detection with the Pixy.
You will use the Pixy to beep when blue is placed in front of the Pixy camera.  You first need to setup signature 1 on
the Pixy to detect blue using Pixymon before starting to implement this module.

You should print out the x, y, width, and height readings from the Pixy (much like the print_pixy_readings example).

If the width reading is greater than 0 then you should make your robot beep.  If you are getting false positives (the 
robot beeps thinking blue is present, but no blue is present) try setting the threshold higher than 0 (see what works
for your environment). After a beep wait for at least 1 second to avoid lots of annoying beeps.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Beep at blue")
    print("--------------------------------------------")
    ev3.Sound.speak("Beep at blue").wait()
    print("Press the touch sensor to exit this program.")

    robot = robo.Snatch3r()
    robot.pixy.mode = "SIG1"

    while not robot.touch_sensor.is_pressed:
        # TODO: 2. Implement the module as described in the opening comment block.
        # It is recommended that you add to your Snatch3r class's constructor the pixy object, as shown
        #   self.pixy = ev3.Sensor(driver_name="pixy-lego")
        #   assert self.pixy
        # Then here you can use a command like width = robot.pixy.value(3)



        time.sleep(0.1)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()

# TODO: 3. Call over a TA or instructor to sign your team's checkoff sheet.
#
# Observations you should make, the Pixy cam can detect colors.  That's just neat. ;)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
