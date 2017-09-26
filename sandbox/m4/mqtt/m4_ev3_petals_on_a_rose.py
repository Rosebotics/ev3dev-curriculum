#!/usr/bin/env python3
"""
This module contains code that needs to run on an EV3 (notice the filename).

You shouldn't look at this code at all.  It's intentionally mysterious and that's part of the fun of this module.
It's a puzzle you have to solve.  If you look at the code it'll give away the fun. :)

All of your coding will be done within m4_pc_petals_on_a_rose.py, open that file.

Author: David Fisher.
"""

# TODO: 1. Have someone on your team run this module on the EV3.  It uses the screen on the EV3.  Whenever you want to
# use the screen you can't just run it via SSH like normal.  You instead have 2 options:
#  chmod +x this file on the EV3 by using the SSH command chmod +x m4_e (hit tab for the rest), then run it via Brickman
#  Temporarily stop Brickman while working on this module, then resume Brickman once complete.
#  Stop via       sudo chvt 6
#  Restart later  sudo chvt 1
# Personally I prefer to stop Brickman and use SSH but either option works.  By doing it the chvt way you get some logs.
#
# Once the program m4_ev3_petals_on_a_rose.py is running on EV3, open m4_pc_petals_on_a_rose.py.
# Don't look at any other code in this file (that's cheating in this game).

import ev3dev.ev3 as ev3
import time
import random
from PIL import Image
import mqtt_remote_method_calls as com


class GameMaster(object):
    """ Delegate that listens for responses from EV3. """

    def __init__(self):
        self.mqtt_client = None
        self.lcd = ev3.Screen()
        self.num_active_dice = 5
        self.max_die_value = 6
        self.consecutive_correct = 0
        self.dice_values = [0, 0, 0, 0, 0]
        self.dice_images = [Image.open('/home/robot/csse120/assets/images/dice/none.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/one.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/two.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/three.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/four.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/five.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/six.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/seven.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/eight.bmp'),
                            Image.open('/home/robot/csse120/assets/images/dice/nine.bmp')]
        self.randomly_display_new_dice()
        self.running = False

    def randomly_display_new_dice(self):
        self.dice_values = [0, 0, 0, 0, 0]
        for i in range(self.num_active_dice):
            self.dice_values[i] = random.randrange(1, self.max_die_value + 1)
        self.update_lcd()

    def update_lcd(self):
        self.lcd.image.paste(self.dice_images[self.dice_values[0]], (5, 8))
        self.lcd.image.paste(self.dice_images[self.dice_values[1]], (62, 8))
        self.lcd.image.paste(self.dice_images[self.dice_values[2]], (119, 8))
        self.lcd.image.paste(self.dice_images[self.dice_values[3]], (33, 66))
        self.lcd.image.paste(self.dice_images[self.dice_values[4]], (91, 66))
        self.lcd.update()

    def loop_forever(self):
        btn = ev3.Button()
        self.running = True
        while not btn.backspace and self.running:
            # Do nothing while waiting for commands
            time.sleep(0.01)
        self.mqtt_client.close()
        # Copied from robot.shutdown
        print("Goodbye")
        ev3.Sound.speak("Goodbye").wait()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

    def guess(self, number_guessed):
        correct_answer = 0
        for value in self.dice_values:
            if value % 2:
                correct_answer += value - 1
                # Even numbers have no stem (dot) in the middle and therefore are not roses.
                # The number 1 has a stem but no "petals" (dots) around it. Value 0
                # The number 3 has a stem and 2 "petals" (dots) around it. Value 2
                # The number 5 has a stem and 4 "petals" (dots) around it. Value 4
                # etc

        if number_guessed == correct_answer:
            print("{} is correct".format(correct_answer))
            if self.num_active_dice == 5:
                self.consecutive_correct += 1
                if self.consecutive_correct >= 3:
                    print("The player has won the game!")
                    self.mqtt_client.send_message("guess_response",
                                                  ["{} is correct! You have won the game!!!!!!!!!!!!!!!!!!".format(
                                                      number_guessed)])
                    ev3.Sound.speak("Correct. You win!").wait()
                    ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav").wait()
                    print("Great work! Now let's make the game a bit harder. :)")
                    self.mqtt_client.send_message("guess_response", ["You are done! You can get your checkoff!"])
                    self.mqtt_client.send_message("guess_response", ["Optional: You can now play with more dots. :)"])
                    self.max_die_value = 9  # Make the game a little harder now.
                    self.consecutive_correct = 0
                else:
                    self.mqtt_client.send_message("guess_response",
                                                  ["{} is correct! You have {} correct in a row.".format(
                                                      number_guessed, self.consecutive_correct)])
                    ev3.Sound.speak("correct")
            else:
                self.consecutive_correct = 0
                self.mqtt_client.send_message("guess_response",
                                              ["{} is correct! To win you need 3 wins WITH 5 DICE!".format(
                                                  number_guessed)])
                ev3.Sound.speak("Correct, but only {} dice.".format(self.num_active_dice))
        else:
            too_high_or_too_low = "Too high" if number_guessed > correct_answer else "Too low"
            self.mqtt_client.send_message("guess_response",
                                          ["Your guess of {} was {}. The correct answer for {} is {}".format(
                                              number_guessed, too_high_or_too_low, self.dice_values, correct_answer)])
            self.consecutive_correct = 0
            ev3.Sound.speak(too_high_or_too_low)
            print(too_high_or_too_low)
        self.randomly_display_new_dice()

    def set_number_of_dice(self, number_of_dice):
        if number_of_dice < 1:
            number_of_dice = 1
        elif number_of_dice > 5:
            number_of_dice = 5
        self.num_active_dice = number_of_dice
        self.randomly_display_new_dice()

    def exit(self):
        self.dice_values = [1, 1, 1, 1, 1]
        self.update_lcd()
        self.running = False


def main():
    print("Ready")
    my_delegate = GameMaster()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()
    # mqtt_client.connect_to_pc("35.194.247.175")  # Off campus use EV3 as broker.
    my_delegate.loop_forever()
    teary_eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_tear.bmp")
    my_delegate.lcd.image.paste(teary_eyes, (0, 0))
    my_delegate.lcd.update()
    print("If you ran via SSH and typed 'sudo chvt 6' earlier, don't forget to type")
    print("'sudo chvt 1' to get Brickman back after you finish this program.")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
