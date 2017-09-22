#!/usr/bin/env python3
"""
For the full problem statement and details see the corresponding m5_pc_remote_drive.py comments.

There are many solutions to this problem.  The easiest solution on the EV3 side is to NOT bother makes a wrapper
class for the robot object.  Since the challenge presented is very direct it's easiest to just use the Snatch3r class
directly as the delegate to the MQTT client.

The code below is all correct.  Only the loop_forever line will fail to compile.  You need to implement that function
in the Snatch3r class in the library (remember the advice from the lecture).  Pick one team member to implement it then
have everyone else Git update.  Additionally you will discover a need to create a method in your Snatch3r class to
support drive and shutdown.

    def drive(self, left_sp, right_sp):
        # Drive the robot forward at the given speeds.

    def loop_forever(self):
        # This is a convenience method that is only useful if the only input to the robot is coming via mqtt.
           MQTT messages will still call methods, but no other input or output happens.

    def shutdown(self):
        # Modify a variable that will allow the loop_forever method to end. Additionally stop motors and set LEDs green.

Once the EV3 code is ready, run it on the EV3 you can work on the PC side code for the MQTT Remote Control.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""
import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    # mqtt_client.connect_to_pc("localhost")  # Off campus use EV3's IP address as broker
    robot.loop_forever()  # Calls a function that has a while True: loop within it to avoid letting the program end.

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
