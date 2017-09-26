#!/usr/bin/env python3
"""
There are no TODOs in this module.  You will simply run this code on your PC to communicate with the EV3.  Feel free
to look at the code to see if you understand what is going on, but no changes are needed to this file.

See the m3_ev3_led_button_communication.py file for all the details.

Author: David Fisher.
"""

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class MyDelegateOnThePc(object):
    """ Helper class that will receive MQTT messages from the EV3. """

    def __init__(self, label_to_display_messages_in):
        self.display_label = label_to_display_messages_in

    def button_pressed(self, button_name):
        print("Received: " + button_name)
        message_to_display = "{} was pressed.".format(button_name)
        self.display_label.configure(text=message_to_display)


def main():
    root = tkinter.Tk()
    root.title("LED Button communication")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_side_label = ttk.Label(main_frame, text="Left LED")
    left_side_label.grid(row=0, column=0)

    left_green_button = ttk.Button(main_frame, text="Green")
    left_green_button.grid(row=1, column=0)
    left_green_button['command'] = lambda: send_led_command(mqtt_client, "left", "green")

    left_red_button = ttk.Button(main_frame, text="Red")
    left_red_button.grid(row=2, column=0)
    left_red_button['command'] = lambda: send_led_command(mqtt_client, "left", "red")

    left_black_button = ttk.Button(main_frame, text="Black")
    left_black_button.grid(row=3, column=0)
    left_black_button['command'] = lambda: send_led_command(mqtt_client, "left", "black")

    button_label = ttk.Label(main_frame, text="  Buttom messages from EV3  ")
    button_label.grid(row=1, column=1)

    button_message = ttk.Label(main_frame, text="--")
    button_message.grid(row=2, column=1)

    right_side_label = ttk.Label(main_frame, text="Right LED")
    right_side_label.grid(row=0, column=2)

    right_green_button = ttk.Button(main_frame, text="Green")
    right_green_button.grid(row=1, column=2)
    right_green_button['command'] = lambda: send_led_command(mqtt_client, "right", "green")

    right_red_button = ttk.Button(main_frame, text="Red")
    right_red_button.grid(row=2, column=2)
    right_red_button['command'] = lambda: send_led_command(mqtt_client, "right", "red")

    right_black_button = ttk.Button(main_frame, text="Black")
    right_black_button.grid(row=3, column=2)
    right_black_button['command'] = lambda: send_led_command(mqtt_client, "right", "black")

    spacer = ttk.Label(main_frame, text="")
    spacer.grid(row=4, column=2)

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client))

    pc_delegate = MyDelegateOnThePc(button_message)
    mqtt_client = com.MqttClient(pc_delegate)
    mqtt_client.connect_to_ev3()
    # mqtt_client.connect_to_ev3("35.194.247.175")  # Off campus IP address of a GCP broker

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter callbacks
# ----------------------------------------------------------------------
def send_led_command(mqtt_client, led_side, led_color):
    print("Sending LED side = {}  LED color = {}".format(led_side, led_color))
    mqtt_client.send_message("set_led", [led_side, led_color])


def quit_program(mqtt_client):
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
