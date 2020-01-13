#!/usr/bin/env python3
"""
This module lets you practice using the buttons on the EV3 as states.

Normally we'll use event callbacks with buttons, but this example uses buttons as states for the purposes of example.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  January 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Have someone on your team run this program as is on the EV3 and make sure everyone understands the code.
# Can you see what the robot does and explain what each line of code is doing? Talk as a group to make sure.

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Buttons and LEDs")
    print("--------------------------------------------")
    ev3.Sound.speak("Buttons and L E Dees").wait()

    # Opening LED dance (to show the LED syntax)
    # Red LEDs
    ev3.Sound.speak("Red")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    time.sleep(3)

    # Green LEDs
    ev3.Sound.speak("Green")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    time.sleep(3)

    # Turn LEDs off
    ev3.Sound.speak("Off")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)
    # ev3.Leds.all_off()  # Could also use this single command if turning both LEDs off.

    # Buttons on EV3 (the real focus of this module)
    btn = ev3.Button()  # Construct the one and only EV3 Button object
    led_colors = [ev3.Leds.BLACK,  # This list is useful for the down button.
                  ev3.Leds.GREEN,
                  ev3.Leds.RED,
                  # ev3.Leds.ORANGE,  # Too close to another color in my opinion
                  # ev3.Leds.YELLOW,  # Too close to another color in my opinion
                  ev3.Leds.AMBER]

    current_color_index = 0
    while True:
        # TODO: 3. Implement the left, right, and up buttons as follows:
        #   When the up button is being pressed, print the word "up" and turn off all LEDs
        #   When the left button is being pressed, print "left", make the LEFT led GREEN, and turn off the right LED
        #   When the right button is being pressed, print "right", make the RIGHT led RED, and turn off the left LED
        #   You are required to use the Button properties for the up, left, and right states, not event callbacks.
        # TODO: 4. Implement the down button to change the color of both LEDs.
        #   The first press to down should make both LEDs GREEN, the next press makes them RED, then AMBER, then off.
        #   If the user presses the down button again, wrap around the list to GREEN and continue as before.
        #   If the user holds down the button, figure out how to make the color change still only happen once.
        #   Since you are only allowed to use states, not event callbacks, this last request is a pain, but it's doable
        #   with a while loop that blocks code execution (simple time.sleep(0.01) in the loop) until released.
        # TODO: 5. Demo your work.
        #
        # Observation you should make, working with button states is functional but usually events work better.

        if btn.left:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)
        if btn.right:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
        if btn.up:
            ev3.Leds.all_off()  # Could also use ev3.Leds.BLACK for both LEDs
        if btn.down:
            current_color_index = (current_color_index + 1) % len(led_colors)
            ev3.Leds.set_color(ev3.Leds.LEFT, led_colors[current_color_index])
            ev3.Leds.set_color(ev3.Leds.RIGHT, led_colors[current_color_index])
            while btn.down:
                time.sleep(0.01)  # Do nothing
        if btn.backspace:
            break
        time.sleep(0.01)  # Best practice to avoid working too hard.

    # Best practice to leave the LEDs on after you finish a program so you don't put away the robot while still on.
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    ev3.Sound.speak("Goodbye").wait()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
