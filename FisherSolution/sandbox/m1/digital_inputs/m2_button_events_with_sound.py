#!/usr/bin/env python3
"""
This module lets you practice using button events with callback functions.

You will use both the simple callback approach, when no additional data needs to be passed, and
the more complex callback approach that uses lamdba when data needs to be shared.

Since this module is all about the buttons the Sound code has just been provided as a finished
example.  You will call different Sound functions using different buttons.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  January 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time


# TODO: 2. Have someone on your team run this program as is on the EV3 and make sure everyone understands the code.
# Can you see what the robot does and explain what each line of code is doing? Talk as a group to make sure.

class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    print("--------------------------------------------")
    print(" Button events with sound")
    print("--------------------------------------------")
    ev3.Sound.speak("Buttons events").wait()

    # Beep is a simple and useful sound.
    ev3.Sound.beep().wait()
    ev3.Sound.beep().wait()

    # Making a simple class is the best way to pass around data between different events.
    dc = DataContainer()

    # Buttons on EV3
    btn = ev3.Button()
    # TODO: 3. Add SIMPLE (no lambda) callbacks for:
    #   .on_up which is connected to a function called handle_up_button(button_state) that exist
    #   .on_down which is connected to a function called handle_down_button(button_state) that exist
    #   .on_left which is connected to a function called handle_left_button(button_state) that exist
    #   .on_right which is connected to a function called handle_right_button(button_state) that exist
    btn.on_up = handle_up_button
    btn.on_down = handle_down_button
    btn.on_left = handle_left_button
    btn.on_right = handle_right_button

    # TODO: 5. Note #4 is lower.  Added a lambda callback for on_backspace.  The syntax of lambda is:
    # button_object.on_backspace = lamdba predefined_inputs(state in this case): function_name(parameters)
    # Using lambda call the function handle_shutdown passing in the state and dc

    # Note there is also an enter button but sometimes that causes issues with Brickman when used
    btn.on_backspace = lambda state: handle_shutdown(state, dc)

    while dc.running:
        btn.process()
        time.sleep(0.01)

    ev3.Sound.speak("Goodbye").wait()


# ----------------------------------------------------------------------
# Button event callback functions
# ----------------------------------------------------------------------

# TODO: 4. Implement the up, down, left, and right callback functions as follows:
#   handle_up_button - when state is true (a press), print the word "up" and call play_song_by_individual_tones()
#   handle_down_button - when state is true (a press), print the word "down" and call play_song_by_notes_list()
#   handle_left_button - when state is true (a press), print the word "left" and call speak()
#   handle_right_button - when state is true (a press), print the word "right" and call play_wav_file()
def handle_up_button(button_state):
    """Handle IR / button event."""
    if button_state:
        print("Up button is pressed")
        play_song_by_individual_tones()
    else:
        print("Up button was released")


def handle_down_button(button_state):
    """Handle IR / button event."""
    if button_state:
        print("Down button is pressed")
        play_song_by_notes_list()
    else:
        print("Down button was released")


def handle_left_button(button_state):
    """Handle IR / button event."""
    if button_state:
        print("Left button is pressed")
        speak()
    else:
        print("Left button was released")


def handle_right_button(button_state):
    """Handle IR / button event."""
    if button_state:
        print("Right button is pressed")
        play_wav_file()
    else:
        print("Right button was released")


# TODO: 6. Implement the handle_shutdown function.
#   Function signature should be:  handle_shutdown(button_state, dc):
#   When the button is pressed (state is true), print the word "back" set dc.running = False
#   Look at the while loop in main to understand why this will end the program.

def handle_shutdown(button_state, dc):
    """Exit the program."""
    if button_state:
        print("Back button is pressed")
        dc.running = False
    else:
        print("Back button was released")


# ----------------------------------------------------------------------
#                           Sound functions
# The 4 functions below have no todos in them. They are finished examples
# of using the ev3.Sound features. Call the right function on button events.
# This can be a handy reference when you want to use your own Sound features.
# Reference http://python-ev3dev.readthedocs.io/en/latest/other.html#sound
# ----------------------------------------------------------------------
def play_song_by_individual_tones():
    """
    Exam of using the ev3.Sound.tone method to play a single tone. For music the ev3.Sound.tone method
    often sounds better with the list approach below. Just showing it doesn't have to be a list.
    """
    tone_map = {"c4": 261.6, "c4s": 277.2, "d4": 293.7, "d4s": 311.1, "e4": 329.6, "f4": 349.2, "f4s": 370.0,
                "g4": 392.0, "g4s": 415.3, "a4": 440, "a4s": 466.2, "b4": 493.9, "c5": 523.3, "c5s": 554.4,
                "d5": 587.3,
                "d5s": 622.3, "e5": 659.3, "f5": 698.5, "f5s": 740.0, "g5": 784.0, "g5s": 830.6, "a5": 880,
                "a5s": 932.3, "b5": 987.8, "c6": 1046.5}

    tempo_ms = 20
    ev3.Sound.tone(tone_map["e5"], tempo_ms * 3).wait()  # Units are in milliseconds
    ev3.Sound.tone(tone_map["e5"], tempo_ms * 6).wait()
    ev3.Sound.tone(tone_map["e5"], tempo_ms * 3).wait()
    time.sleep(tempo_ms / 1000 * 3)  # Units are in seconds so divide by 1000
    ev3.Sound.tone(tone_map["c5"], tempo_ms * 3).wait()
    ev3.Sound.tone(tone_map["e5"], tempo_ms * 6).wait()
    ev3.Sound.tone(tone_map["g5"], tempo_ms * 12).wait()
    ev3.Sound.tone(tone_map["g4"], tempo_ms * 12).wait()
    # Didn't add the rest of the song to make testing faster.


def play_song_by_notes_list():
    """
    Pass in a list of notes to the ev3.Sound.tone method
    From: http://python-ev3dev.readthedocs.io/en/latest/other.html#sound

    List of tuples, where each tuple contains up to three numbers.
    The first number is frequency in Hz, the second is duration in milliseconds, and the
    third is delay in milliseconds between this and the next tone in the sequence.
    """
    ev3.Sound.tone([
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100)  # Commented out the rest of the song to make testing faster.

        # , (587.32, 350, 100), (587.32, 350, 100),
        # (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        # (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
        # (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        # (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        # (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100),
        # (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
        # (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        # (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100),
        # (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100),
        # (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
        # (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        # (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        # (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200),
        # (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        # (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
    ]).wait()


def speak():
    """
    Example of using the speak command.  This is probably the most useful ev3.Sound feature.

    """
    ev3.Sound.speak("Everything is awesome!")  # This version does not wait for the sound to complete to continue
    # ev3.Sound.speak("Everything is awesome!").wait()  # This version blocks future code execution until complete.


def play_wav_file():
    # File from http://www.moviesoundclips.net/ev3.Sound.php?id=288
    # Had to convert it to a PCM signed 16-bit little-endian .wav file
    # http://audio.online-convert.com/convert-to-wav
    ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
