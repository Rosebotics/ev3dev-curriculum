#!/usr/bin/env python3
"""
This module lets you practice EV3 drive motor commands using timed delays.

Use input prompts to get the target speed (degrees per second) and desired time to drive from the user.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Get a yardstick or tape measure to do some testing with /examples/motors/drive_input_speed.py
#   Have your whole team work this activity together.
#   For speeds 100, 200, ... 900 record how far the robot moves in 5 seconds, then divide that number by 5. Record below
#   For example if 400 degrees per second (dps) when 30 inches in 5 seconds, then 400 dps = 6 inches per second
#   100 degrees / second  -->  999 inches / second
#   200 degrees / second  -->  999 inches / second
#   300 degrees / second  -->  999 inches / second
#   400 degrees / second  -->  999 inches / second
#   500 degrees / second  -->  999 inches / second
#   600 degrees / second  -->  999 inches / second
#   700 degrees / second  -->  999 inches / second
#   800 degrees / second  -->  999 inches / second
#   900 degrees / second  -->  999 inches / second
#   Derive from that information an equation that would allow you to input any distance in inches and any speed in
#     degrees per second, then output the time needed to drive at that speed to travel the correct distance.
#   Hint: Use a rough approximation equation to determine inches/second from a given degrees/second, then use the
#     target distance (inches) divided by the speed (inches/second) to get seconds needed.  If you like you are welcome
#     to use a tool like Excel's trendline feature but that is overkill, does not have to be perfect!!!
# TODO: 3. Copy the content of the /examples/motors/drive_input_speed.py program and place it below these comments.
# TODO: 4. Change the input questions from:
#   Enter a speed for the left motor (0 to 900 dps):
#   Enter a speed for the right motor (0 to 900 dps):
#   Enter a time to drive (seconds):
# to:
#   Enter a speed (0 to 900 dps):
#   Distance to travel (inches):
# TODO: 5. Write the code necessary to make the robot drive at that speed going roughly that distance.
#   Note you are REQUIRED to use the pattern... run_forever() time.sleep(some_amount) stop()
#   For this module you may NOT use the advanced motor commands run_to_abs_pos, run_to_rel_pos, or run_timed.
# TODO: 6. Modify the program so that it will exit immediately if the answer to any question is 0 (wait until concept).
# TODO: 7. Formally test your work. When you think you have the problem complete run these tests:
# 200 dps 24 inches (make sure it drives within 6 inches of the target distance)
# 400 dps 24 inches (make sure it drives within 6 inches of the target distance)
# 800 dps 24 inches (make sure it drives within 6 inches of the target distance)
# 400 dps 12 inches (make sure it drives within 3 inches of the target distance)
# 400 dps 36 inches (make sure it drives within 9 inches of the target distance)
# Add more tests as you see fit.  Ideally you should be +/- 25% of the target goal.
#
# Observation you should make, the pattern run_forever-->time.sleep-->stop naturally blocks code execution until done.

