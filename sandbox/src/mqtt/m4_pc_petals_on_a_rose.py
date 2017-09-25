#!/usr/bin/env python3
"""
The goal for this module is to interact with your EV3 using MQTT.  You will only write code on the PC side this time.
You will need to run the m4_ev3_petals_on_a_rose.py on your EV3, but you don't need to modify that file (you don't even
need to ever open that file).  Your EV3 is acting as a puzzle, your goal is to use MQTT to solve the puzzle.

The way the puzzle works is that five dice roll and somehow they combine to a single number.
You need to figure out the pattern and win the game.  To win the game you must...

Correctly guess the number 3 times in a row (while using 5 dice).

Don't plan to win by random guessing, try to figure out the pattern. Before you can figure out the pattern though, first
you need to write the code to make guesses.  Additionally if you write more code you can tell the EV3 how to change the
number of dice to help you figure out the pattern more quickly.

To check off this part of the assignment win the game (without looking at the EV3 code).

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


# TODO: 2. Create a class. Feel free to call it MyDelegate.
# Within that class you don't even need an __init__ constructor (an empty constructor comes for free)

# TODO: 3. Create a method named guess_response within MyDelegate.
# guess_response needs to receive self and a string, feel free to call the string parameter message_from_ev3
# within the body of the method print message_from_ev3.  That's it.  You simply need to hear what EV3 tells you.


def main():
    # TODO: 4. Create a my_delegate object from your MyDelegate class
    # Create an mqtt_client object from the com.MqttClient class passing in my_delegate
    # connect_to_ev3

    root = tkinter.Tk()
    root.title("Petals on a Rose")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    label = ttk.Label(main_frame, text='Look at the EV3, then enter a guess for the solution:')
    label.grid(columnspan=2)

    guess_entry = ttk.Entry(main_frame, width=8)
    guess_entry.grid(row=2, column=0)

    guess_button = ttk.Button(main_frame, text="Guess")
    guess_button.grid(row=2, column=1)
    guess_button['command'] = lambda: guess(mqtt_client, guess_entry)
    root.bind('<Return>', lambda event: guess(mqtt_client, guess_entry))

    num_dice_entry = ttk.Entry(main_frame, width=8)
    num_dice_entry.grid(row=3, column=0)

    num_dice_button = ttk.Button(main_frame, text="Set num dice")
    num_dice_button.grid(row=3, column=1)
    num_dice_button['command'] = lambda: set_num_dice(mqtt_client, num_dice_entry)

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=4, column=0)
    q_button['command'] = lambda: quit_program(mqtt_client, False)

    e_button = ttk.Button(main_frame, text="Exit on EV3 too")
    e_button.grid(row=4, column=1)
    e_button['command'] = lambda: quit_program(mqtt_client, True)

    root.mainloop()


def guess(mqtt_client, number_to_guess_entry):
    """ Calls a method on EV3 called 'guess' passing in an int from the number_to_guess_entry. """
    # TODO: 5. Uncomment the line of code below to make guesses with EV3.
    # mqtt_client.send_message("guess", [int(number_to_guess_entry.get())])
    number_to_guess_entry.delete(0, 'end')
    # Note: You can play the game with only TO DO 5 complete, but it will be easier to solve if you do TO DO 6 as well.


def set_num_dice(mqtt_client, num_dice_entry):
    """ Calls a method on EV3 called 'set_number_of_dice' passing in an int from the num_dice_entry. """
    # TODO: 6. Write the line of code necessary to implement this method based on the doc string's description.


# TODO: 7. See if you can solve the mystery.  Based on the dice how can you solve Petals on a Rose?
# To check off this part of the assignment figure out the pattern and win the game (without looking at the EV3 code).


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        mqtt_client.send_message("exit")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
