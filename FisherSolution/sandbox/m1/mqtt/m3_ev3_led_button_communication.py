#!/usr/bin/env python3
"""
The goal of this module is to practice doing MQTT communication.  In this module you will only write code that runs on
the EV3.  The code that runs on the PC (m3_pc_led_button_communication.py) is already written for you.  You will need to
implement this module, run it on your EV3, then at the same time run m3_pc_led_button_com.py on your computer to do the
communication.  Summary of the communication:

  EV3 receiving:
      The EV3 will have a delegate that has a method called "set_led" which receives two strings:
        led_side_string (the first parameter) will be either "left" or "right"
        led_color_string (the second parameter) will be either "green", "red", or "black"
      When the EV3 receives a set_led message from the PC it will set the appropriate LED to the appropriate color.
      Warning, the strings must be converted into appropriate values before using the ev3.Leds.set_color method.

  EV3 sending:
      The EV3 will send an mqtt message to the PC whenever the Up, Down, Left, or Right button is pressed on the EV3.
      The method name sent will be "button_pressed" which will have 1 parameter (sent as a List with 1 item)
         The parameter sent in the List will be the value "Up", "Down", "Left", or "Right"

  PC receiving:
      The PC will have a delegate that has a method called "button_pressed" which receives 1 string:
        button_name (the only parameter) will be either "Up", "Down", "Left", or "Right"
        That method is already done and it displays the result to the Tkinter gui window.

  PC sending:
      The PC will send an mqtt message to the EV3 whenever a Tkinter button is clicked.
      The method name sent will be "set_led" which will have 2 parameters (sent as a List with 2 items)
        The first parameter will be either "left" or "right"
        The second parameter will be either "green", "red", or "black"
      That method is already done and it will send when buttons are clicked on the Tkinter GUI.

Implement the TODOs below to complete this module.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  January 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import time


class MyDelegate(object):

    def __init__(self):
        self.running = True

    # TODO: 2. Prepare the one and only delegate method, set_led, to receive messages as described above.
    # Here is some code that will likely be useful in this method to convert the led_side_string and led_color_string
    # into a useful led_side and led_color values that can be used with the ev3.Leds.set_color method.
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

    def set_led(self, led_side_string, led_color_string):
        """Sets the LED to the appropriate color."""

        led_side = None
        if led_side_string == "left":
            led_side = ev3.Leds.LEFT
        elif led_side_string == "right":
            led_side = ev3.Leds.RIGHT

        led_color = None
        if led_color_string == "green":
            led_color = ev3.Leds.GREEN
        elif led_color_string == "red":
            led_color = ev3.Leds.RED
        elif led_color_string == "black":
            led_color = ev3.Leds.BLACK

        if led_side is None or led_color is None:
            print("Invalid parameters sent to set_led. led_side_string = {} led_color_string = {}".format(
                led_side_string, led_color_string))

        ev3.Leds.set_color(led_side, led_color)


def main():
    print("--------------------------------------------")
    print(" LED Button communication")
    print(" Press Back to exit when done.")
    print("--------------------------------------------")
    ev3.Sound.speak("LED Button communication").wait()

    # TODO: 3. Create a delegate (an instance of the class above) and an MQTT client, passing in the delegate
    # Once you have that done connect the mqtt_client.
    # To help you out this time you simply need to uncomment the code below.
    #
    # my_delegate = MyDelegate()
    # mqtt_client = com.MqttClient(my_delegate)
    # mqtt_client.connect_to_pc()
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_pc()

    # Buttons on EV3
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

        # TODO 4: Send a message using MQTT that will:
        #   - Call the method called "button_pressed" on the delegate at the other end of the pipe.
        #   - Pass the parameters [button_name] as a list.
        # This is meant to help you learn the mqtt_client.send_message syntax.
        mqtt_client.send_message("button_pressed", [button_name])


# TODO 5: Run this program on your EV3 and run m3_pc_led_button_communication.py on your PC.
# Click the Tkinter buttons on your PC and watch the LEDs on the EV3
# Press the buttons on the EV3 (up, down, left, right) and watch the Tkinter GUI on your PC.
# When done, press the Back button on EV3 to end that program and click Quit on the Tkinter GUI.

def handle_shutdown(button_state, my_delegate):
    """Exit the program."""
    if button_state:
        my_delegate.running = False


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
