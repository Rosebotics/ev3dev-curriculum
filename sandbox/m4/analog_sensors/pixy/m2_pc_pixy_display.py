"""
There are no TODOs in this module. This module will run on your PC. It will receive information from your Pixy camera
and display the Pixy readings visually on the screen. The EV3 needs to read the Pixy sensor and then send over the
information for the x, y, width, and height.  The code you write will be in the m2_ev3_pixy_display module and it will
run on the EV3.  You can look at this module to see what message the PC is expecting to receive.  It is expecting an
MQTT call to:

  on_rectangle_update       with the parameters         [x, y, width, height]

When that message is received, it will update the rectangle that is displayed on the canvas to match the Pixy values.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""

import tkinter
from tkinter import ttk


import mqtt_remote_method_calls as com


class MyDelegate(object):

    def __init__(self, canvas, rectangle_tag):
        self.canvas = canvas
        self.rectangle_tag = rectangle_tag

    def on_rectangle_update(self, x, y, width, height):
        self.canvas.coords(self.rectangle_tag, [x, y, x + width, y + height])


def main():
    root = tkinter.Tk()
    root.title = "Pixy display"

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    # The values from the Pixy range from 0 to 319 for the x and 0 to 199 for the y.
    canvas = tkinter.Canvas(main_frame, background="lightgray", width=320, height=200)
    canvas.grid(columnspan=2)

    rect_tag = canvas.create_rectangle(150, 90, 170, 110, fill="blue")

    # Buttons for quit and exit
    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=3, column=1)
    quit_button["command"] = lambda: quit_program(mqtt_client)

    # Create an MQTT connection
    my_delegate = MyDelegate(canvas, rect_tag)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()
    # mqtt_client.connect_to_ev3("35.194.247.175")  # Off campus IP address of a GCP broker

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter event handler
# ----------------------------------------------------------------------
def quit_program(mqtt_client):
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
