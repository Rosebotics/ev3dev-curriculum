#!/usr/bin/env python3
"""
The goal of this module is to practice doing MQTT communication.  In this module you will only write code that runs on
the EV3.  The code that runs on the PC (m3_pc_led_button_communication.py) is already written for you.  You will need to
implement this module, run it on your EV3, then at the same time run m3_pc_led_button_com.py on your computer to do the
communication.  Summary of the communication:

  EV3 receiving (you will be writing this code in this module, running it on EV3):
      The EV3 will have a delegate that has a method called "set_led" which receives two strings:
        led_side_string (the first parameter) will be either "left" or "right"
        led_color_string (the second parameter) will be either "green", "red", or "black"
      When the EV3 receives a set_led message from the PC it will set the appropriate LED to the appropriate color.
      Warning, the strings must be converted into appropriate values before using the ev3.Leds.set_color method.

  EV3 sending (you will be writing this code in this module, running it on EV3):
      The EV3 will send an mqtt message to the PC whenever the Up, Down, Left, or Right button is pressed on the EV3.
      The method name sent will be "button_pressed" which will have 1 parameter (sent as a List with 1 item)
         The parameter sent will be the either ["Up"], ["Down"], ["Left"], or ["Right"] (always a List with 1 item)

  PC receiving (this code is already complete in m3_pc_led_button_communication.py, which will run on your PC):
      The PC will have a delegate that has a method called "button_pressed" which receives 1 string:
        button_name (the only parameter) will be either "Up", "Down", "Left", or "Right"
        That method is already done and it displays the result to the Tkinter gui window.

  PC sending (this code is already complete in m3_pc_led_button_communication.py, which will run on your PC):
      The PC will send an mqtt message to the EV3 whenever a Tkinter button is clicked.
      The method name sent will be "set_led" which will have 2 parameters (sent as a List with 2 items)
        The first parameter will be either "left" or "right"
        The second parameter will be either "green", "red", or "black"
      That method is already done and it will send when buttons are clicked on the Tkinter GUI.

Implement the TODOs below to complete this module, then transfer the file to the EV3 (as done in many previous units),
  then run this module on the EV3 while at the same time, running m3_pc_led_button_communication.py on your PC.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import time


# TODO: 2. Within the MyDelegate class below add the method, set_led, to receive messages as described above.
# Here is some code that will likely be VERY useful in that method to convert the led_side_string and led_color_string
#   into a useful led_side and led_color values that can be used with the ev3.Leds.set_color method.
#
#     print("Received: {} {}".format(led_side_string, led_color_string))
#     led_side = None
#     if led_side_string == "left":
#         led_side = ev3.Leds.LEFT
#     elif led_side_string == "right":
#         led_side = ev3.Leds.RIGHT
#
#     led_color = None
#     if led_color_string == "green":
#         led_color = ev3.Leds.GREEN
#     elif led_color_string == "red":
#         led_color = ev3.Leds.RED
#     elif led_color_string == "black":
#         led_color = ev3.Leds.BLACK
#
#     if led_side is None or led_color is None:
#         print("Invalid parameters sent to set_led. led_side_string = {} led_color_string = {}".format(
#             led_side_string, led_color_string))
#     else:
#         ev3.Leds.set_color(led_side, led_color)

class MyDelegate(object):

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")
    print(" LED Button communication")
    print(" Press Back to exit when done.")
    print("--------------------------------------------")
    ev3.Sound.speak("LED Button communication").wait()

    # TODO: 3. Create an instance of your delegate class and an MQTT client, passing in the delegate object.
    # Note: you can determine the variable names that you should use by looking at the errors underlined in later code.
    # Once you have that done connect the mqtt_client to the MQTT broker using the connect_to_pc method.
    # Note: on EV3 you call connect_to_pc, but in the PC code it will call connect_to_ev3


    # Buttons on EV3 (these obviously assume TO DO: 3. is done)
    btn = ev3.Button()
    btn.on_up = lambda state: handle_button_press(state, mqtt_client, "Up")
    btn.on_down = lambda state: handle_button_press(state, mqtt_client, "Down")
    btn.on_left = lambda state: handle_button_press(state, mqtt_client, "Left")
    btn.on_right = lambda state: handle_button_press(state, mqtt_client, "Right")
    btn.on_backspace = lambda state: handle_shutdown(state, my_delegate)

    while my_delegate.running:
        btn.process()
        time.sleep(0.01)

    ev3.Sound.speak("Goodbye").wait()
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)


# ----------------------------------------------------------------------
# Button event callback functions
# ----------------------------------------------------------------------
def handle_button_press(button_state, mqtt_client, button_name):
    """Handle IR / button event."""
    if button_state:
        print("{} button was pressed".format(button_name))

        # TODO: 4. Send a message using MQTT that will:
        #   -- Call the method called "button_pressed" on the delegate at the other end of the pipe.
        #   -- Pass the parameters [button_name] as a list.
        # This is meant to help you learn the mqtt_client.send_message syntax.
        # You can review the code above to understand how button_name is passed into this function.


# TODO: 5. Run this program on your EV3 and run m3_pc_led_button_communication.py on your PC at the same time.
# This will be the first time you've run a program on the robot today, but you'll remember how to do it (right?).
# Hint: To be less confusing use two different computers for this task.  One to run the EV3 program (you) and one to run
#   the PC program (a different person on your team).  It can be done from one computer but that gets confusing.
# Click the Tkinter buttons on your PC and watch the LEDs on the EV3
# Press the buttons on the EV3 (up, down, left, right) and watch the Tkinter GUI on your PC.
# When done, press the Back button on EV3 to end that program and click Quit on the Tkinter GUI.

# TODO: 6. Call over a TA or instructor to sign your team's checkoff sheet (demo both LEDs and buttons).
#
# Observations you should make, when communicating using MQTT there is always a program running on EV3 and on your PC
#   at the same time.  To make your life easier, you only write one of those programs this time (the on on the EV3).
#   We try to use the naming convention m#_pc and m#_ev3 to show where the program should run since it gets confusing.


def handle_shutdown(button_state, my_delegate):
    """Exit the program."""
    if button_state:
        my_delegate.running = False


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
