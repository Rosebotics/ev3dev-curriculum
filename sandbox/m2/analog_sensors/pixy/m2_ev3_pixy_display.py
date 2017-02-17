#!/usr/bin/env python3
"""
The goal of this module is to practice using the Pixy and MQTT at the same time.  This module will send data from the
EV3 to the PC.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Pixy display")
    print(" Press the touch sensor to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("Pixy display").wait()

    # TODO: 2. Create an MqttClient (no delegate needed since EV3 will only send data, so an empty constructor is fine)
    # Then connect to the pc using the connect_to_pc method.




    robot = robo.Snatch3r()
    # Add the pixy property to that Snatch3r class so that it is available in your library.

    while not robot.touch_sensor.is_pressed:

        # TODO: 3. Read the Pixy values for x, y, width, and height
        # Print the values (much like the print_pixy_readings example)

        # TODO: 4. Send the Pixy values to the PC by calling the on_rectangle_update method
        # If you open m2_pc_pixy_display you can see the parameters for that method [x, y, width, height]




        time.sleep(0.25)

    ev3.Sound.speak("Goodbye")
    mqtt_client.close()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

