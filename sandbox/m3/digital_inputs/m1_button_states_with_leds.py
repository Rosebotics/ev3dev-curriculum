#!/usr/bin/env python3
"""
This module lets you practice using the buttons on the EV3 as states.

Normally we'll use event callbacks with buttons, but this example uses buttons as states for the purposes of example.
Much like we did in m1 of the motors unit, later we will show you different (better) ways to use buttons.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Have someone on your team run this program as is on the EV3 and make sure everyone understands the code.
#   You will exit the program by pressing the back button on the EV3 brick (button just below the screen).
#   The back button is already implemented to exit the program (as you can see in the code below).

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
    print('Press the Back button on the EV3 to exit this program.')

    # Buttons on EV3 (the real focus of this module)
    btn = ev3.Button()  # Construct the one and only EV3 Button object
    led_colors = [ev3.Leds.BLACK,  # This list is useful for the down button in TO DO 4.
                  ev3.Leds.GREEN,
                  ev3.Leds.RED,
                  # ev3.Leds.ORANGE,  # Too close to another color in my opinion
                  # ev3.Leds.YELLOW,  # Too close to another color in my opinion
                  ev3.Leds.AMBER]

    current_color_index = 0
    while True:
        # TODO: 3. Implement the left, right, and up buttons as follows:
        #    When the up button is being pressed:
        #      -- print the word "up"
        #      -- turn off all LEDs
        #    When the left button is being pressed:
        #      -- print the word "left"
        #      -- make the LEFT led GREEN
        #      -- turn off the right LED
        #    When the right button is being pressed:
        #      -- print "right"
        #      -- make the RIGHT led RED
        #      -- turn off the left LED
        #   You are required to use the Button instance variables for the up, left, and right (not event callbacks).
        #   Notice that the word "up" (or "left" or "right" is printed continually while you hold the button)
        #   Optional: You can also comment out the code above that does the 6 second red, green, off pattern.  It was
        #     there just to provide you with code examples for using the LEDs.  It does not need to run anymore.
        #     Just make sure not to comment out too much. ;)

        # TODO: 4. Implement the down button to change the color of both LEDs.
        #   The first press to down should make both LEDs GREEN, the next press makes them RED, then AMBER, then off.
        #   If the user presses the down button again, wrap around the list to GREEN and continue as before.
        #   If the user holds down the button, figure out how to make the color change still only happen once.
        #   Since you are only allowed to use states, not event callbacks, this last request is a pain, but it's doable
        #     with a while loop that blocks code execution until the down instance variable is False.
        #     Use a time.sleep(0.01) inside the while loop to do nothing but wait for the button to be released.

        # TODO: 5. Formally test your work. When you think you have the problem complete run these tests:
        #   Press Left - Green left LED is on (try holding the button down for a few seconds when you to the press)
        #   Press Right - Right right LED is on
        #   Press Up - Both LEDs are off
        #   Press Down - Both LEDs are Green
        #   Press Down - Both LEDs are Red
        #   Press Down - Both LEDs are Amber (try holding the button down for a few seconds when you to the press)
        #   Press Down - Both LEDs are off
        #   Press Down - Both LEDs are Green
        #   Press Down - Both LEDs are Red (the cycle repeats)
        #   Press Back - Both LEDs turn Green, the robot says Goodbye and the program exits

        # TODO: 6. Call over a TA or instructor to sign your team's checkoff sheet and do a code review.
        #
        # Observation you should make, working with buttons as 'states' is functional but usually 'events' work better.
        # Also observe that we don't use the Enter button.  Enter can cause issues since your program is running at the
        #   same time as the Brickman operating system.  Both are receiving the button events.  That can be changed, but
        #   it's too much trouble to do here.  So instead we just don't use the Enter button.

        if btn.backspace:
            break
        time.sleep(0.01)  # Best practice to have a short delay to avoid working too hard between loop iterations.

    # Best practice to leave the LEDs on after you finish a program so you don't put away the robot while still on.
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
