"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import time

import math


class PixyBlock(object):
    """Model object class that holds Pixy readings"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def size(self):
        return self.width * self.height

    def __repr__(self):
        return "x: {} y: {} width: {} height: {}".format(self.x, self.y, self.width, self.height)


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    SNATCH3R_ARM_REVS = 14.2
    SNATCH3R_ARM_DEGS = SNATCH3R_ARM_REVS * 360

    # Full range of speeds is -900 to +900
    SLOW_SPEED = 200
    MEDIUM_SPEED = 400
    FAST_SPEED = 700
    MAX_SPEED = 900

    def __init__(self):
        self.running = False

        # Connect two large motors on output ports B and C and medium motor on A
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)

        # Check that the motors are actually connected
        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected

        # Connect the four sensors to input ports 1-4
        self.touch_sensor = ev3.TouchSensor()  # address=in1
        self.pixy = ev3.Sensor(driver_name="pixy-lego")  # address=in2:i2c1
        self.color_sensor = ev3.ColorSensor()  # address=in3
        self.ir_sensor = ev3.InfraredSensor()  # address=in4

        # Check that all the sensors are actually connected
        assert self.touch_sensor
        assert self.pixy
        assert self.color_sensor
        assert self.ir_sensor

        # self.calibrate_arm() # Could require a calibration on every initialization
        # ev3.Sound.speak("Ready")  # Most of the programs speak themselves so not needed.
        time.sleep(0.1)  # Found that sometimes the ir_sensor needed a moment before using it.

    def drive(self, left_sp, right_sp):
        """ Drive the robot forward at the given speeds. """
        self.left_motor.run_forever(speed_sp=left_sp)
        self.right_motor.run_forever(speed_sp=right_sp)

    def drive_inches(self, inches_target, speed_deg_per_second=MEDIUM_SPEED):
        """ Drives the robot a fixed number of inches. """
        degrees_per_inch = 91
        motor_turns_deg = inches_target * degrees_per_inch
        self.left_motor.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=speed_deg_per_second, stop_action="brake")
        self.right_motor.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=speed_deg_per_second, stop_action="brake")
        time.sleep(0.1)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")

    def turn_degrees(self, degrees_to_turn, turn_speed_sp=MEDIUM_SPEED):
        """ Helper method that turns a set number of degrees. """
        motor_degrees_to_turn = 486 / 90 * degrees_to_turn
        self.left_motor.run_to_rel_pos(position_sp=-motor_degrees_to_turn, speed_sp=turn_speed_sp, stop_action="brake")
        self.right_motor.run_to_rel_pos(position_sp=motor_degrees_to_turn, speed_sp=turn_speed_sp, stop_action="brake")
        # Note, that there is no delay using the commands above, so we much wait
        self.left_motor.wait_while("running")  # Wait for the turn to finish
        self.right_motor.wait_while("running")  # Wait for the turn to finish

    def stop(self):
        self.left_motor.stop(stop_action="coast")
        self.right_motor.stop(stop_action="coast")

    def arm_calibration(self):
        """Runs the arm up until the touch sensor is hit then back down (beeping at both locations).
           Intended to be run with nothing in the jaws, but that isn't critical."""
        self.arm_motor.run_forever(speed_sp=self.MAX_SPEED)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep().wait()
        self.arm_motor.run_to_rel_pos(position_sp=-self.SNATCH3R_ARM_DEGS)
        time.sleep(0.1)  # See warning for wait_until on http://python-ev3dev.readthedocs.io/en/latest/motors.html
        self.arm_motor.wait_while("running")
        self.arm_motor.position = 0  # Calibrate the down position as 0.
        ev3.Sound.beep().wait()

    def arm_up(self):
        """Moves the Snatch3r arm to the up position."""
        self.arm_motor.run_forever(speed_sp=self.MAX_SPEED)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep().wait()

    def arm_down(self):
        """Moves the Snatch3r arm to the down position."""
        self.arm_motor.run_to_abs_pos(position_sp=0, stop_action="coast", speed_sp=self.MAX_SPEED)
        time.sleep(0.1)  # See warning for wait_until on http://python-ev3dev.readthedocs.io/en/latest/motors.html
        self.arm_motor.wait_while("running")  # Blocks until the motor finishes running
        ev3.Sound.beep().wait()

    def seek_beacon(self, beacon_channel=1):
        """ Drives to the beacon"""

        # Set the value for the sensor readings based on the IR remote channel
        # See http://www.ev3dev.org/docs/sensors/lego-ev3-infrared-sensor/
        heading_value_index = 2 * (beacon_channel - 1)
        distance_value_index = 1 + 2 * (beacon_channel - 1)

        self.ir_sensor.mode = "IR-SEEK"
        forward_speed = 300
        turn_speed = 100
        distance_0_readings = 0

        while not self.touch_sensor.is_pressed:
            time.sleep(0.1)
            current_distance = self.ir_sensor.value(distance_value_index)
            if current_distance == 100:
                print("IR Remote not found")
                # self.stop()
                self.drive(-turn_speed, turn_speed)
                continue
            current_heading = self.ir_sensor.value(heading_value_index)
            if math.fabs(current_heading) < 2:
                # Close enough of a heading to move forward
                if current_distance > 0:
                    self.drive(forward_speed, forward_speed)
                elif current_distance == 0:
                    self.stop()
                    distance_0_readings += 1
                    if distance_0_readings > 5:
                        print("I got the beacon")
                        break  # Success!
            else:
                if math.fabs(current_heading) > 10:
                    print("Heading is too far off to fix, just spin: ", current_heading)
                    self.drive(-turn_speed, turn_speed)
                elif current_heading < 0:
                    self.drive(-turn_speed, turn_speed)
                else:
                    self.drive(turn_speed, -turn_speed)

    def set_pixy_color_signature(self, signature):
        """Sets the color signature that will be returned by calls to get_pixy_block"""
        if signature == 1:
            self.pixy.mode = "SIG1"
        elif signature == 2:
            self.pixy.mode = "SIG2"
        elif signature == 3:
            self.pixy.mode = "SIG3"
        elif signature == 4:
            self.pixy.mode = "SIG4"
        elif signature == 5:
            self.pixy.mode = "SIG5"
        elif signature == 6:
            self.pixy.mode = "SIG6"
        elif signature == 7:
            self.pixy.mode = "SIG7"
        else:
            print("Invalid signature value")

    def get_pixy_block(self):
        """Returns information about what the Pixy camera is viewing.
           For more see: http://www.ev3dev.org/docs/sensors/charmed-labs-pixy-cmucam5-for-lego/
            value1: X
            value2: Y
            value3: Width
            value4: Height"""
        return PixyBlock(self.pixy.value(1), self.pixy.value(2), self.pixy.value(3), self.pixy.value(4))

    def get_ir_distance(self):
        return self.ir_sensor.proximity

    def loop_forever(self):
        """This is a convenience method that I don't really recommend for most programs.
           This method is only useful if the only input to the robot is coming via mqtt.
           MQTT messages will still call methods, but no other input or output happens."""
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing until the robot does a shutdown.

    def shutdown(self, exit_program=True):
        """Close the program"""
        print("Goodbye")
        self.left_motor.stop(stop_action="coast")
        self.right_motor.stop(stop_action="coast")
        self.arm_motor.stop(stop_action="coast")
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Sound.speak("Goodbye").wait()
        self.running = False  # Just in case the loop_forever method was used.
        if exit_program:
            exit()
