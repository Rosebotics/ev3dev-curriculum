#!/usr/bin/env python3
"""
Contains example code snippets used in the drive motor lecture.  Don't try to actually run this file!
These are just snippets used in the lecture, not actual code to run!

TODO: 1. PASSIVELY LISTEN TO THE LECTURE ABOUT MQTT
https://docs.google.com/presentation/d/1gQt1K4X2xzcspKMn2S0X98vhzVNmLA-xoQe5rp58CVE/edit?usp=sharing

Author: David Fisher
"""

import ev3dev.ev3 as ev3
import time

import robot_controller as robo
import mqtt_remote_method_calls as com


def sending_messages_to_ev3():
    """ Example of connecting from a PC to the EV3 and sending commands.
        This does not necessarily show best practice, just showing syntax."""
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    mqtt_client.send_message("arm_up")
    time.sleep(4)
    mqtt_client.send_message("arm_down")
    time.sleep(4)
    for _ in range(4):
        mqtt_client.send_message("drive_inches", [24, 500])
        time.sleep(4.4)
        mqtt_client.send_message("turn_degrees", [90, 300])
        time.sleep(3)
        mqtt_client.send_message("beep")


def receiving_messages_from_pc():
    """ Example of connecting from an EV3 to the PC and sending commands.
        This does not necessarily show best practice, just showing syntax."""
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()  # Avoids letting the robot finish until some "end" command.

    # Pretend like the Snatch3r class has these methods.  The other end can say "shutdown"
    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing until the robot does a shutdown.

    def shutdown(self):
        ev3.Sound.speak("Goodbye").wait()
        self.running = False


def using_a_robot_wrapper_class():
    """ A more recommended way to connect from EV3 to the PC using a wrapper Delegate class.
        I think making your own class that HAS A robot is the best approach to use in most apps."""

    class MyDelegate(object):
        def __init__(self):
            self.robot = robo.Snatch3r()
            self.mqtt_client = None  # To be set later.

        def arm_up(self):
            print("Arm up")
            self.robot.arm_up()

        def drive_square(self, side_length, speed):
            for _ in range(4):
                self.robot.drive_inches(side_length, speed)
                self.robot.turn_degrees(90, speed)

        def loop_forever(self):
            btn = ev3.Button()
            while not btn.backspace:
                # do stuff
                time.sleep(0.01)
            if self.mqtt_client:
                self.mqtt_client.close()
            self.robot.shutdown()

    def main():
        my_delegate = MyDelegate()
        mqtt_client = com.MqttClient(my_delegate)
        my_delegate.mqtt_client = mqtt_client
        mqtt_client.connect_to_pc()
        my_delegate.loop_forever()
        print("Shutdown complete.")

    main()


def the_computer_can_receive_messages_too():
    """ Showing an example of a PC receiving a message.  This code is similar to m1 but not
        identical, so don't copy anything from here except maybe the words:
          mqtt_client.send_message("on_circle_draw", [        ])
        """

    # Make a quick custom class.
    class MyDelegate(object):
        def __init__(self, canvas):
            self.canvas = canvas

        def on_circle_draw(self, color, x, y):
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color, width=3)

    canvas = "A Tkinter object"  # Something specific to the m1_pc_shared_circles example.
    my_delegate = MyDelegate(canvas)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect("draw", "draw")

    time.sleep(2)
    mqtt_client.send_message("on_circle_draw", ['blue', 50, 50])

    time.sleep(5)
    mqtt_client.close()
