#!/usr/bin/env python3
"""
Contains example code snippets used in the drive motor lecture.  Don't try to actually run this file!
These are just snippets used in the lecture, not actual code to run!

TODO: 1. PASSIVELY LISTEN TO THE LECTURE ABOUT DIGITAL INPUTS (and a few other things)
https://docs.google.com/presentation/d/1mUxsC-cUO4S5bwhTAQG0G10IO0gsbAU5YEORxeh0mMc/edit?usp=sharing

Author: David Fisher
"""

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


def touch_sensor_as_state():
    """Example of using the TouchSensor with a state."""
    touch_sensor = ev3.TouchSensor()
    assert touch_sensor
    for _ in range(10):
        if touch_sensor.is_pressed:
            print("Touch sensor is pressed")
        else:
            print("Touch sensor is not pressed")
        time.sleep(1.0)


def buttons_as_states():
    """Example of using buttons with states."""
    btn = ev3.Button()
    for _ in range(10):
        if btn.left:
            print("Left is pressed")
        elif btn.right:
            print("Right is pressed")
        elif btn.up:
            print("Up is pressed")
        elif btn.down:
            print("Down is pressed")
        elif btn.backspace:
            print("Back is pressed")
        else:
            print("No button pressed")
        time.sleep(1.0)


def buttons_as_events():
    """Example of using buttons with events + callbacks"""

    def handle_up_down_button(state):
        if state:
            print("Up or down was pressed")
        else:
            print("Up or down was released")

    # Buttons on EV3
    btn = ev3.Button()
    btn.on_up = handle_up_down_button
    btn.on_down = handle_up_down_button
    # Also use btn.on_left, btn.on_right, btn.on_backspace

    while True:
        # Note, you can exit the program via Ctrl-c within SSH
        btn.process()
        time.sleep(0.01)


def buttons_as_events_using_lambda():
    """Example of using buttons with events + callbacks with lambda"""

    def handle_up_down_button(state, name):
        if state:
            print(name, "was pressed")
        else:
            print(name, "was released")

    # Buttons on EV3
    btn = ev3.Button()
    btn.on_up = lambda state: handle_up_down_button(state, "Up")
    btn.on_down = lambda state: handle_up_down_button(state, "Down")
    # Also use btn.on_left, btn.on_right, btn.on_backspace

    while True:
        btn.process()
        time.sleep(0.01)


def button_events_using_lambda():
    """Example of using buttons with events + callbacks with lambda"""

    def handle_up_down_button(state, name):
        if state:
            print(name, "was pressed")
        else:
            print(name, "was released")

    # Buttons on EV3
    btn = ev3.Button()
    btn.on_up = lambda state: handle_up_down_button(state, "Up")
    btn.on_down = lambda state: handle_up_down_button(state, "Down")
    # Also use btn.on_left, btn.on_right, btn.on_backspace

    while True:
        btn.process()
        time.sleep(0.01)


def button_events_using_lambda_with_objects():
    """Example of using buttons with events + callbacks with lambda using objects"""

    class DataContainer(object):
        """ Helper class that might be useful to communicate between different callbacks."""

        def __init__(self):
            self.running = True

    def handle_arm_up_button(button_state, my_robot):
        """Moves the arm up when the button is pressed."""
        if button_state:
            my_robot.arm_up()

    def handle_shutdown(button_state, dc):
        """Exit the program."""
        if button_state:
            dc.running = False

    # Buttons on EV3
    btn = ev3.Button()
    robot = robo.Snatch3r
    dc = DataContainer()
    btn.on_up = lambda state: handle_arm_up_button(state, robot)
    btn.on_backspace = lambda state: handle_shutdown(state, dc)

    while dc.running:
        btn.process()
        time.sleep(0.01)


def leds_example():
    """Basic LED example"""
    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    for _ in range(100):
        time.sleep(0.1)
        if touch_sensor.is_pressed:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.ORANGE)
        else:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.ORANGE)

    ev3.Leds.all_off()  # The lines below can be used to turn off only 1 LED if you need that.
    # ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    # ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)


def sound_examples():
    """Example Sound commands """
    ev3.Sound.beep()

    tone_time_ms = 20
    delay_time_ms = 50
    ev3.Sound.tone(440, tone_time_ms).wait()
    time.sleep(delay_time_ms / 1000)
    ev3.Sound.tone(523, tone_time_ms).wait()

    # Recommended approach for songs
    ev3.Sound.tone([(440, tone_time_ms, delay_time_ms),
                    (523, tone_time_ms, delay_time_ms)]).wait()

    ev3.Sound.speak("Ready").wait()
    ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav")


def ir_remote_example(dc):
    """Example of setting up an IR Remote button, shows only 1 but the pattern is easy to follow for more."""

    def handle_red_up_1(button_state, dc):
        if button_state:
            print("Down button is pressed")
            dc.do_something()
        else:
            print("Down button was released")

    rc1 = ev3.RemoteControl(channel=1)
    assert rc1.connected
    rc1.on_red_up = lambda state: handle_red_up_1(state, dc)
    # rc1.on_red_down = lambda state: handle_red_down_1(state, dc)
    # rc1.on_blue_up = lambda state: handle_blue_up_1(state, dc)
    # rc1.on_blue_down = lambda state: handle_blue_down_1(state, dc)


def screen_example():
    """Shows the commands to add a full screen image.  There is more you could do with the screen, but not the focus
       here.  Look online to learn more. https://sites.google.com/site/ev3python/learn_ev3_python/screen"""
    from PIL import Image
    lcd_screen = ev3.Screen()

    image = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_angry.bmp")
    lcd_screen.image.paste(image, (0, 0))
    lcd_screen.update()


def touchsensor_example():
    """Core code that is used to move the arm to the up position."""
    arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
    touch_sensor = ev3.TouchSensor()

    arm_motor.run_forever(speed_sp=900)
    while not touch_sensor.is_pressed:
        time.sleep(0.01)
    arm_motor.stop(stop_action="brake")
