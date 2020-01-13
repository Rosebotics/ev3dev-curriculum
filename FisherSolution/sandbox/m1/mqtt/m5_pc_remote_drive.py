#!/usr/bin/env python3
"""
This module is the mini-project for the MQTT unit.  This module will be running on your PC and communicating with the
m5_ev3_remote_drive.py module that is running on your EV3 (you have to write that module too, but it's easier).
Only the Tkinter GUI has been made for you.  You will need to implement all of the MQTT communication.  The goal is to
have a program running on your computer that can control the EV3.

You will need to have the following features:
  - Clickable drive direction buttons to drive forward (up), backwards (down), left, right, and stop (space)
    - Keyboard shortcut keys that behave the same as clicking the buttons (this has already been wired up for you)
  - An entry box for the left and right drive motor speeds.
    - If both become set to 900 all of the drive direction buttons will go fast, for example forward goes 900 900
    - If both become set to 300 all of the drive direction buttons will go slower, for example reverse goes -300 -300
    - If to 500 then left does -500 500, which causes the robot to spin left (can also use half speed -250 250 if fast)
    - If set differently to say 600 left, 300 right the robot will drive and arc, for example forward goes 600 300
  - In addition to the drive features there needs to be a clickable button for Arm Up and Arm Down
    - There also need to be keyboard shortcut for Arm Up (u) and Arm Down (j).  Arm calibration is not required.

  - Finally you need 2 buttons for ending your program:
    - Quit, which stops only this program and allows the EV3 program to keep running
    - Exit, which sends a shutdown message to the EV3 then ends it's own program as well.

You can start by running the code to see the GUI, but don't expect button clicks to do anything useful yet.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  January 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    # TODO: 2. Setup an mqtt_client.  Notice that since you don't need to receive any messages you do NOT need to have
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    # mqtt_client.connect_to_ev3("104.154.136.22")  # Off campus use EV3's IP address as broker

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # TODO: 3. Implement the callbacks for the drive buttons. Set both the click and shortcut key callbacks.
    # forward_button['command'] = lambda: some_callback1(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Up>', lambda event: same_callback_as_above1(mqtt_client, left_speed_entry, right_speed_entry))
    forward_button['command'] = lambda: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, 1, 1)
    root.bind('<Up>', lambda event: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, 1, 1))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button['command'] = lambda: some_callback2(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Left>', lambda event: same_callback_as_above2(mqtt_client, left_speed_entry, right_speed_entry))
    left_button['command'] = lambda: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, -0.5, 0.5)
    root.bind('<Left>', lambda event: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, -0.5, 0.5))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button['command'] = lambda: some_callback3(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Right>', lambda event: same_callback_as_above3(mqtt_client, left_speed_entry, right_speed_entry))
    right_button['command'] = lambda: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, 0.5, -0.5)
    root.bind('<Right>', lambda event: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, 0.5, -0.5))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button['command'] = lambda: some_callback4(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Down>', lambda event: same_callback_as_above4(mqtt_client, left_speed_entry, right_speed_entry))
    back_button['command'] = lambda: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, -1, -1)
    root.bind('<Down>', lambda event: send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, -1, -1))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Optional extra key press features to turn small set amounts left or right. You are not required to implement this.
    root.bind('<a>', lambda event: send_turn_amount(mqtt_client, 20))
    root.bind('<s>', lambda event: send_turn_amount(mqtt_client, 10))
    root.bind('<d>', lambda event: send_turn_amount(mqtt_client, -10))
    root.bind('<f>', lambda event: send_turn_amount(mqtt_client, -20))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter callbacks
# ----------------------------------------------------------------------
# TODO: 4. Implement the functions for the drive button callbacks.
def send_drive_command(mqtt_client, left_speed_entry, right_speed_entry, left_direction, right_direction):
    left_sp = left_direction * int(left_speed_entry.get())
    right_sp = right_direction * int(right_speed_entry.get())
    print("drive", [left_sp, right_sp])
    mqtt_client.send_message("drive", [left_sp, right_sp])


def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


# This is the optional method
def send_turn_amount(mqtt_client, turn_amount):
    print("turn_degrees", [turn_amount])
    mqtt_client.send_message("turn_degrees", [turn_amount])


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
