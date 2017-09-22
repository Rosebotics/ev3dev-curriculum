This folder contains only sound and image file assets. These assets are used in various modules throughout the curriculum.

This folder needs to be uploaded to your robot before the sound and image files can be used.
It is recommended that one team member right clicks on the project folder to upload the entire project to the robot at least once when the project begins.  During that upload these files will be transferred to the EV3 brick and then they will be available to all modules for use.
Once on the robot this folder will be at the path:<br>
/home/robot/csse120/assets/

Here is an example of using image or sound files:

        eyes_img = Image.open("/home/robot/csse120/assets/images/ev3_lego/eyes_neutral.bmp")

        ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav")