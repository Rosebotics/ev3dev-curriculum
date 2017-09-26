"""
The goal for this module is to show that usually in our MQTT communication we will send messages to one recipient and
that same recipient will be sending messages back to us.  This module also runs only on your PC and has very few todo
items.  You will simply be setting your name and you will be selecting one person on your team to send messages to.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class MyDelegate(object):

    def __init__(self, label):
        self.label = label

    def on_chat_message(self, message):
        self.label["text"] += "\n" + message


def main():
    # TODO: 2. Set my_name and set team_member_name then try this program with that person.
    # For teams of 3 just have 2 people talk to each other and the other person can just watch this time.
    my_name = "Dave"  # Used to set the topic that you are *subscribed to* listen to
    team_member_name = "Dave"  # Used to set the topic that you will *publish to*

    # What happens if you set my_name and team_member_name to the same value?
    # The goal is simply for you to become more comfortable with how subscriptions and publish work with MQTT
    # Review the code to see if there are any other useful things you can learn.

    # TODO: 3. Call over a TA or instructor to sign your team's checkoff sheet.
    #
    # Observations you should make:
    # You published messages to "legoXX/{team_member_name}"  (where XX is set in libs/mqtt_remote_method_calls.py)
    # You subscribed to messages for  "legoXX/{my_name}"
    # So only MQTT clients listening for that name will hear, and you only hear messages sent to you.
    # Later you'll publish messages to your EV3 and subscribe to messages that your EV3 sends.

    root = tkinter.Tk()
    root.title = "MQTT PyChat"

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    label = ttk.Label(main_frame, justify=tkinter.LEFT, text="Send a message to " + team_member_name)
    label.grid(columnspan=2)

    msg_entry = ttk.Entry(main_frame, width=60)
    msg_entry.grid(row=2, column=0)

    msg_button = ttk.Button(main_frame, text="Send")
    msg_button.grid(row=2, column=1)
    msg_button['command'] = lambda: send_message(mqtt_client, my_name, chat_window, msg_entry)
    root.bind('<Return>', lambda event: send_message(mqtt_client, my_name, chat_window, msg_entry))

    chat_window = ttk.Label(main_frame, justify=tkinter.LEFT, text="", width=60, wraplength="500p")
    # chat_window.pack(fill="x")
    chat_window.grid(columnspan=2)

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=4, column=1)
    q_button['command'] = (lambda: quit_program(mqtt_client))

    # Create an MQTT connection
    my_delegate = MyDelegate(chat_window)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(my_name, team_member_name)
    # mqtt_client.connect(my_name, team_member_name, "35.194.247.175")  # Off campus IP address of a GCP broker

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter event handlers
# ----------------------------------------------------------------------
def send_message(mqtt_client, my_name, chat_window, msg_entry):
    msg = msg_entry.get()
    msg_entry.delete(0, 'end')
    chat_window["text"] += "\nMe: " + msg
    mqtt_client.send_message("on_chat_message", [my_name + ": " + msg])


def quit_program(mqtt_client):
    if mqtt_client:
        mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
