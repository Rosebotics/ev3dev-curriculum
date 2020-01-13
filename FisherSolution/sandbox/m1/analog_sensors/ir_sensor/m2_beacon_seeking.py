#!/usr/bin/env python3
"""
The goal of this module is to drive towards the beacon (the IR remote in beacon mode) and stop your robot right in front
of the beacon.  To put the IR Remote into beacon mode, press the button at the top of the remote and make sure the green
LED is on. Use channel 1 for this module.

Your program will call a function called seek_beacon that will run until the distance to the beacon is 0.  Once that
function gets the robot to that location it will stop the robot and return.  Within the main function the user will be
prompted if they want to find the beacon again (presumably you move it first) or quit.


Authors: David Fisher and PUT_YOUR_NAME_HERE.  February 2017.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.
import traceback

import ev3dev.ev3 as ev3
import time
import math

import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Beacon seeking")
    print("--------------------------------------------")
    ev3.Sound.speak("Beacon seeking")

    robot = robo.Snatch3r()
    try:
        while True:
            seek_beacon(robot)
            ev3.Sound.speak("Found the beacon")
            command = input("Hit enter to seek the beacon again or enter q to quit: ")
            if command == "q":
                break
    except:
        traceback.print_exc()
        ev3.Sound.speak("Error")

    robot.shutdown()


def seek_beacon(robot):
    """ Uses the IR Sensor in IR-SEEK mode to find the beacon."""

    # TODO: 2. Uncomment the line below to put the robot's IR sensor into IR-SEEK mode.
    robot.ir_sensor.mode = "IR-SEEK"

    forward_speed = 300
    turn_speed = 100

    # Set the value for the sensor readings based on the IR remote channel
    # See http://www.ev3dev.org/docs/sensors/lego-ev3-infrared-sensor/
    heading_value_index = 0
    distance_value_index = 1

    while not robot.touch_sensor.is_pressed:
        # The touch sensor can be used to abort the attempt (sometimes handy during testing)
        current_heading = robot.ir_sensor.value(heading_value_index)
        current_distance = robot.ir_sensor.value(distance_value_index)
        if current_distance == 100:
            print("IR Remote not found. Distance: ", current_distance)
            robot.stop()
        else:

            # TODO: 3. Implement the following strategy to find the beacon.
            # If the absolute value of the current_heading is less than 2, you are on the right heading.
            #     If the current_distance is 0 return from this function, you have found the beacon!
            #     If the current_distance is greater than 0 drive straight forward (forward_speed, forward_speed)
            # If the absolute value of the current_heading is NOT less than 2 but IS less than 10, you need to spin
            #     If the current_heading is less than 0 turn left (-turn_speed, turn_speed)
            #     If the current_heading is greater than 0 turn right  (turn_speed, -turn_speed)
            # If the absolute value of current_heading is greater than 10 stop and print Heading too far off
            #
            # Using that plan you should find the beacon if the beacon is in range.  If the beacon is not in range your
            # robot should just sit still until the beacon is placed into view.  It is recommended that you always print
            # something each pass through the loop to help you debug what is going on.  Examples:
            #    print("On the right heading. Distance: ", current_distance)
            #    print("Adjusting heading: ", current_heading)
            #    print("Heading is too far off to fix: ", current_heading)


            if math.fabs(current_heading) < 2:
                # Close enough of a heading to move forward
                print("On the right heading. Distance: ", current_distance)
                if current_distance > 0:
                    robot.drive(forward_speed, forward_speed)
                else:
                    robot.stop()
                    return
            elif math.fabs(current_heading) < 10:
                # Close enough to adjust
                print("Adjusting heading: ", current_heading)
                if current_heading < 0:
                    robot.drive(-turn_speed, turn_speed)
                else:
                    robot.drive(turn_speed, -turn_speed)
            else:
                print("Heading is too far off to fix: ", current_heading)
                robot.stop()

        time.sleep(0.2)
    robot.stop()  # In case the touch_sensor was pressed to abort.

    # TODO: 4. Demo your program by putting the beacon within a few feet of the robot, within 30 degrees of straight in
    # front.  The robot should drive to and stop at the beacon.  After a successful run move the beacon then do it again
    # for the demo.  During testing if your robot fails to find the beacon remember that you can press the touch sensor
    # to abandon ship on the attempt. ;)  You must demo 2 successful finds in a row to check off.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
