"""
The goal for this module is to ease you into learning the MQTT library api (the MqttClient class within
libs/mqtt_remote_method_calls.py). To make your life easier many of the TODOs in this module simply say to
"uncomment the code below".  This code is run on your computer and does not use an EV3 robot at all.

The goal is for you to think about how the MQTT library works.  You need to:
 -- Create a class to serve as your message recipient (your delegate)
 -- Construct an instance of your delegate class and construct an instance of the MqttClient class
    -- Pass the instance of your delegate class into the MqttClient constructor
 -- Call one of the .connect methods on the MqttClient object to connect to the MQTT broker
    -- The connect method you use will establish what topic you are publishing to and what topic you are subscribing to.
 -- Use the send_message command to call methods on the delegate that is on the opposite end of the pipe.

In addition to the MQTT goals, this example will show some tkinter tricks:
  -- How to capture mouse clicks and process the X Y locations
  -- How to draw circles onto a Tkinter Canvas.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


# TODO: 2. Select one team member to open libs/mqtt_remote_method_calls.py and complete the TO DO that is in that file.
# After making that change, they should commit their work and all other team members should do a VCS -> Update
# After all team members see that file changed you can move on to the next TO DO
# Also someone should update the libs/mqtt_remote_method_calls.py file on the robot too (at some point before m3).

# TODO: 3. Run this program as is on your computer and watch the logs as you click in the window.
# Next see if you can review the code to see how it works.  You can do this individually or as a team.


import tkinter
from tkinter import ttk


# TODO: 4. Uncomment the code below.  It imports a library and creates a relatively simple class.
# The constructor receives a Tkinter Canvas and the one and only method draws a circle on that canvas at a given XY.

# import mqtt_remote_method_calls as com
#
#
# class MyDelegate(object):
#
#     def __init__(self, canvas):
#         self.canvas = canvas
#
#     def on_circle_draw(self, color, x, y):
#         self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color, width=3)


def main():
    root = tkinter.Tk()
    root.title = "MQTT Shared Circles"

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    instructions = "Click the window to make a circle"
    label = ttk.Label(main_frame, text=instructions)
    label.grid(columnspan=2)

    # Make a tkinter.Canvas on a Frame.
    canvas = tkinter.Canvas(main_frame, background="lightgray", width=800, height=500)
    canvas.grid(columnspan=2)

    # Make callbacks for mouse click events.
    canvas.bind("<Button-1>", lambda event: left_mouse_click(event, mqtt_client))

    # Make callbacks for the two buttons.
    clear_button = ttk.Button(main_frame, text="Clear")
    clear_button.grid(row=3, column=0)
    clear_button["command"] = lambda: clear(canvas)

    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=3, column=1)
    quit_button["command"] = lambda: quit_program(mqtt_client)

    # Create an MQTT connection
    # TODO: 5. Delete the line below (mqtt_client = None) then uncomment the code below.  It creates a real mqtt client.
    mqtt_client = None
    # my_delegate = MyDelegate(canvas)
    # mqtt_client = com.MqttClient(my_delegate)
    # mqtt_client.connect("draw", "draw")

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter event handlers
# Left mouse click
# ----------------------------------------------------------------------
def left_mouse_click(event, mqtt_client):
    """ Draws a circle onto the canvas (one way or another). """
    print("You clicked location ({},{})".format(event.x, event.y))

    # TODO: 6. Talk to your team members and have everyone pick a unique color.
    # Examples... "red", "green", "blue", "yellow", "aquamarine", "magenta", "navy", "orange"
    my_color = "magenta"  # Make your color unique

    # Optional test: If you just want to see circles purely local to your computer the four lines below would work.
    # You could uncomment it to see it temporarily, but make sure to comment it back out before todo7 below.
    # canvas = event.widget
    # canvas.create_oval(event.x - 10, event.y - 10,
    #                    event.x + 10, event.y + 10,
    #                    fill=my_color, width=3)
    # Repeated: If you uncommented the code above to test it, make sure to comment it back out before todo7 below.

    # MQTT draw
    # TODO: 7. Send a message using MQTT that will:
    #   - Call the method called "on_circle_draw" on the delegate at the other end of the pipe.
    #   - Pass the parameters [my_color, event.x, event.y] as a list.
    # This is the only TO DO you have to think about.  It is meant to help you learn the mqtt_client.send_message syntax
    # Review the lecture notes about the two parameters passed into the mqtt_client.send_message method if needed
    # All of your teammates should receive the message and create a circle of your color at your click location.
    # Additionally you will receive your own message and draw a circle in your color too.

    # TODO: 8. Help get everyone on your team running this program at the same time.
    # You should be able to see circles on your computer from everyone else on your team.
    # Try to draw the first letter of your name in circles. :)

    # TODO: 9. Call over a TA or instructor to sign your team's checkoff sheet.
    #
    # Observations you should make, with MQTT your team can hear your messages.
    # You published messages to the "legoXX/draw" topic (where XX is the number set in libs/mqtt_remote_method_calls.py)
    # You subscribed to messages for the "legoXX/draw" topic (so you are talking to yourself and others)
    # Later you'll publish messages to your EV3 and subscribe to messages that your EV3 sends.


# ----------------------------------------------------------------------
# Tkinter event handlers
# The two buttons
# ----------------------------------------------------------------------
def clear(canvas):
    """Clears the canvas contents"""
    canvas.delete("all")


def quit_program(mqtt_client):
    """For best practice you should close the connection.  Nothing really "bad" happens if you
       forget to close the connection though. Still it seems wise to close it then exit."""
    if mqtt_client:
        mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
