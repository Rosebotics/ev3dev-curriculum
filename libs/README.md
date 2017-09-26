This is a special folder that will contain two modules:
- mqtt_remote_method_calls.py - Finished module that has only a single TODO which should be completed by team member #1.  This module is a helper module that will be used when you get to the MQTT communication exercises.
- robot_controller.py  - Empty file that you will implement through the exercises.  This code is shared by everyone on the team.  You should create helper methods for your robot and add them to this module.  Then everyone on the team can use those methods.  This library will be useful for the exercises and it should be used in your project as well.

On the robot this folder will be at the location:<br>
/home/robot/csse120/libs

This exact folder path is important since it has manually been added to the PYTHONPATH on each robot, via this command in the .bashrc file
**export PYTHONPATH="/home/robot/csse120/libs"**  These two modules are available on the robot from any location.

**TODO: 1.** The libs folder is available **on the robot** from any location already, however PyCharm on your computer does not know that yet.
So you need to right click on the libs folder, then select Mark Directory as --> Sources Root.
By doing that PyCharm will help you with code completion when calling methods in this folder.
Each member of the team should do that step now, but only 1 person needs to mark the TODO as DONE.