#!/usr/bin/env python3
"""
This module lets you practice EV3 drive motor commands using timed delays.

Use input prompts to get the target speed (degrees per second) and desired number of inches from the user.
Then make the EV3 drive a given number of inches at the target speed.  You will need to do some experiments
to collect data, then make an equation to figure out the time needed given the distance and speed.

Note: If future modules you will learn different (BETTER) ways to drive a given distance.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Get a yardstick or tape measure to do some testing with /examples/motors/drive_input_speed.py
#   Have your whole team work this activity together.
#   For speeds 100, 200, ... 900 record how many inches the robot moves in 10 seconds, then divide that number by 10 to
#     get the speed of the robot in inches per second.
#   For example if you used the drive_input_speed.py example to do a test at 200 degrees per second (dps) for 10 seconds
#     and it went 30 inches in those 10 seconds, then 200 dps = 3 inches per second.
#   Note there is nothing magic about 10 seconds, it's just that 1 second is too short to be accurate.  You could use 5
#     second tests and just divide the distance by 5.
#
#  Record your calculated speed conversions here:
#   100 degrees / second  -->  999 inches / second
#   200 degrees / second  -->  999 inches / second
#   300 degrees / second  -->  999 inches / second
#   400 degrees / second  -->  999 inches / second
#   500 degrees / second  -->  999 inches / second
#   600 degrees / second  -->  999 inches / second
#   700 degrees / second  -->  999 inches / second
#   800 degrees / second  -->  999 inches / second
#   900 degrees / second  -->  999 inches / second
#
# TODO: 3. Make an equation
#   Derive from that information a way to convert a given degrees per second speed into an inches / second speed.
#     Eventually your goal is to make an equation that will allow users to input any distance in inches and any speed in
#     degrees per second, then output the time needed to drive the correct distance at that speed.  So eventually you
#     will be making a formula like this... (for now just think about how to convert degrees/sec to in/sec)
#
#   Time (seconds) = Distance (inches, as input from the user) / Speed (inches/second, as converted based on user input)
#
#   Note: To repeat again, in later modules you will learn different (better) ways to travel a given distance using
#     motor encoders, so just make a simple rough approximation here, since later we'll do it better in a different way.
#
# TODO: 3. Copy the content of the /examples/motors/drive_input_speed.py program and place it below these comments.
# TODO: 4. Change the input questions from:
#   Enter a speed for the left motor (0 to 900 dps):
#   Enter a speed for the right motor (0 to 900 dps):
#   Enter a time to drive (seconds):
# to:
#   Enter a speed (0 to 900 dps):
#   Distance to travel (inches):
# TODO: 5. Write the code necessary to make the robot drive at that speed going roughly that distance.
#   Note, in this module, you are REQUIRED to use the pattern...
#      run_forever()
#      time.sleep(some_amount)
#      stop()
#   You may NOT use the advanced motor commands at this time like: run_to_abs_pos, run_to_rel_pos, or run_timed.
# TODO: 6. Modify the program so that it will exit immediately if the answer to any question is 0.
# TODO: 7. Formally test your work. When you think you have the problem complete run these tests:
#   200 dps 24 inches (make sure it drives within 6 inches of the target distance)
#   400 dps 24 inches (make sure it drives within 6 inches of the target distance)
#   800 dps 24 inches (make sure it drives within 6 inches of the target distance)
#   400 dps 12 inches (make sure it drives within 3 inches of the target distance)
#   400 dps 36 inches (make sure it drives within 9 inches of the target distance)
# Do more tests if you see fit.  Ideally you should be +/- 25% of the target goal.
#
# TODO: 8. Call over a TA or instructor to sign your team's checkoff sheet and do a code review.
#
#  Observation you should make, the pattern run_forever-->time.sleep-->stop naturally blocks code execution until done.
