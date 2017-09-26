#!/usr/bin/env python3
"""
In this module you'll practice using the IR Remote using event callbacks.  You'll find the process works the same
as buttons.  There are 6 buttons (up, down, left, right, enter, and back) and 16 IR remote buttons (4 buttons *
4 channels).  We will only use lambda callbacks for this example since that is the easiest way to do everything once
you are comfortable with the lambda syntax.

Your task will be to display different images on the screen when certain IR buttons are pressed.  Working with the
screen is easy if you use the `chmod +x m3_ir_events_with_the_screen.py` command, then run the program from the Brickman
interface.  If you want to use SSH to run the program though you first need to stop the Brickman programming from
running so that your screen images stay visible for more than 1 second.  You can keep the Brickman UI program stopped
until you complete this problem.

To stop the Brickman interface type:
  sudo chvt 6
When prompted for the password - C$$E120

To restart the Brickman interface after you complete this problem type:
  sudo chvt 1
Which will probably not require you to type the password since sudo was just run earlier.

BTW chvt means CHange the Virtual Terminal, and 86ing something means to kick it out.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time
from PIL import Image


# TODO: 2. Have someone on your team run this program as is on the EV3 and make sure everyone understands the code.
# Can you see what the robot does and explain what each line of code is doing? Talk as a group to make sure.

class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True

        # Creates the one and only Screen object and prepares a few Image objects.
        self.lcd_screen = ev3.Screen()

        # All of these images are exactly 178 by 128 pixels, the exact screen resolution
        # They are made by Lego and ship with the Lego Mindstorm EV3 Home Edition software
        self.eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_neutral.bmp")
        self.angry_eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_angry.bmp")
        self.puppy_dog_eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_disappointed.bmp")
        self.sad_eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_hurt.bmp")
        self.shifty_eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_pinch_left.bmp")
        self.progress_0 = Image.open("/home/robot/csse120/assets/images/ev3_lego/progress_bar_0.bmp")
        self.progress_50 = Image.open("/home/robot/csse120/assets/images/ev3_lego/progress_bar_50.bmp")
        self.progress_100 = Image.open("/home/robot/csse120/assets/images/ev3_lego/progress_bar_100.bmp")
        self.teary_eyes = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_tear.bmp")


def main():
    print("--------------------------------------------")
    print(" IR Events with the Screen")
    print("--------------------------------------------")
    print("Exit this program with the Back button.")
    # You will notice very few print commands in this module since this module uses the screen.
    # If you run Screen programs on the EV3 using Brickman, print commands go to that screen too which causes ugly
    # screen images. If you run Screen programs via SSH print commands work as expected.

    # Object that is storing references to images that can be passed into callbacks.
    dc = DataContainer()

    display_image(dc.lcd_screen, dc.eyes)  # Display an image on the EV3 screen
    ev3.Sound.speak("I R events with the Screen").wait()

    # TODO: 3. Create a remote control object for channel 1. Add lambda callbacks for:
    #   .on_red_up    to call handle_red_up_1    (that exist already) with state and dc as parameters
    #   .on_red_down  to call handle_red_down_1  (that exist already) with state and dc as parameters
    #   .on_blue_up   to call handle_blue_up_1   (that exist already) with state and dc as parameters
    #   .on_blue_down to call handle_blue_down_1 (that exist already) with state and dc as parameters

    # TODO: 5. Create remote control objects for channels 2, 3, and 4. Add lambda callbacks for on_red_up to each one:
    #   Channel 2's .on_red_up should call handle_red_up_2 (that exist already) with state and dc as parameters
    #   Channel 3's .on_red_up should call handle_red_up_3 (that exist already) with state and dc as parameters
    #   Channel 4's .on_red_up should call handle_red_up_4 (that exist already) with state and dc as parameters

    # Buttons on EV3
    btn = ev3.Button()
    btn.on_backspace = lambda state: handle_shutdown(state, dc)

    while dc.running:
        # TODO: 4. Call the .process() method on your channel 1 RemoveControl object, then review and run your code.
        #   Review the handle functions below to see how they draw to the screen.  They are already finished.

        # TODO: 6. Call the .process() method on your channel 2 - 4 RemoveControl objects and demo your code.
        #   Review the handle functions below to see how they draw to the screen.  They are already finished.

        # TODO: 7. Call over a TA or instructor to sign your team's checkoff sheet and do a code review.
        #
        # Observations you should make, IR buttons work exactly like buttons on the EV3.
        #   The screen is a bit annoying to work with due to the Brickman OS interference.
        #   Note you could've run this program with Brickman too, but screen draws would last one 1 second each.

        btn.process()  # Monitors for the Back button to exit the program if called.
        time.sleep(0.01)

    # When the program completes (the user hit the Back button), display a crying image and say goodbye.
    display_image(dc.lcd_screen, dc.teary_eyes)
    ev3.Sound.speak("Goodbye").wait()
    print("If you ran via SSH and typed 'sudo chvt 6' earlier, don't forget to type")
    print("'sudo chvt 1' to get Brickman back after you finish this program.")


# ----------------------------------------------------------------------
# IR Remote callbacks
# ----------------------------------------------------------------------
def handle_red_up_1(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.angry_eyes)


def handle_red_down_1(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.puppy_dog_eyes)


def handle_blue_up_1(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.sad_eyes)


def handle_blue_down_1(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.shifty_eyes)


def handle_red_up_2(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.progress_0)


def handle_red_up_3(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.progress_50)


def handle_red_up_4(button_state, dc):
    """
    Handle IR event.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        display_image(dc.lcd_screen, dc.progress_100)


# ----------------------------------------------------------------------
# Shutdown callback
# ----------------------------------------------------------------------
def handle_shutdown(button_state, dc):
    """
    Exit the program.

    Type hints:
      :type button_state: bool
      :type dc: DataContainer
    """
    if button_state:
        dc.running = False


# ----------------------------------------------------------------------
# Helper Screen function for putting an image on the screen.
# ----------------------------------------------------------------------
def display_image(lcd_screen, image):
    """
    Helper function to put an image on the screen.  All images used with this function should be full screen images.
    The screen is 178 by 128 pixels.  In this module we're using ones that came from Lego that are full screen.
    Smaller images can be used as well and the upper left corner does not always need to be 0, 0.

    Type hints:
      :type lcd_screen: ev3.Screen
      :type image: Image
    """
    lcd_screen.image.paste(image, (0, 0))
    lcd_screen.update()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
