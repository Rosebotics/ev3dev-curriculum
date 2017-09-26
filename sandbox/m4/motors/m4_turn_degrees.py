"""
This module lets you extend what you have learned about driving and extend it to turning.

Much like you have a drive_inches command in your library, you will now make a turn_degrees method.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Copy the contents of m3_drive_inches_via_library.py and paste that text into this file below these comments.
#   Change the initial print and speak commands to reflect this module, like this...
#     print("--------------------------------------------")
#     print(" Turn degrees")
#     print("--------------------------------------------")
#     ev3.Sound.speak("Turn degrees").wait()
#   You will need to modify that code for this problem, but it is a handy starting point.

# TODO: 3. Create a method in your library called turn_degrees that receives the degrees_to_turn and turn_speed_sp
#   To help you get started here is a potential method signature line that will be in your library.
#
#   def turn_degrees(self, degrees_to_turn, turn_speed_sp):
#
#   Develop your code as a team within the robot_controller.py file and make sure all team member understand it.
#   MAKE SOMEONE DIFFERENT TYPE!  You may not allow the same person to type that typed the drive_inches method.
#   In that library method:
#     To make a left turn (positive degrees_to_turn values) at a given turn_speed_sp set the left wheel to
#       speed_sp=-turn_speed_sp and the right wheel to speed_sp=turn_speed_sp.
#     To make right turns (negative degrees_to_turn values) use speed_sp=-turn_speed_sp on the right and
#       speed_sp=turn_speed_sp on the left.
#     Use the run_to_rel_pos, .wait_while(ev3.Motor.STATE_RUNNING) pattern to implement your work (not timed driving)
#   You will have to experimentally determine the formula for accurate position_sp turn amounts.

# TODO: 4. Individually implement the code here to use your turn_degrees library method.
#   Modify the code to ask the user how many degrees they would like to turn
#   Ask the user what speed they would like to use for the turn (0 to 900 degrees per second).
#   Beep after the turn is complete via a beep in this module (tests to make sure the library is blocking)
#   When the library method is complete have all team members VCS update and test using their own m4_turn_degrees.py

# TODO: 5. Formally test your work. When you think you have the problem complete run these tests:
#     45 degrees turns left 45 degrees
#    -45 degrees turn right 45 degrees putting you back where you started
#     90 degrees turns left 90 degrees
#    -90 degrees turn right 90 degrees putting you back where you started
#    180 degrees
#   -180 degrees
#    360 degrees
# Add more tests as you see fit.  Ideally you should be within 45 degrees of back where you started (if you can).

# TODO: 6. Call over a TA or instructor to sign your team's checkoff sheet and do a code review.
#
# Observations you should make, using run_to_rel_pos is useful for accurate turns, but testing takes time.
