This repository is meant to be a tool for helping you learn to program the Lego EV3 Mindstorms robot with Python.<br>
Some background information will be provided here with links to other documentation.  The assumption is that before
you begin using **this** repository to learn ev3-python you first have setup your Lego Mindstorm EV3 with ev3dev as
discussed in the **Background information**.

## Background information
Typically the EV3 is programmed with a block based programming language that is available for Windows and OS X.<br>
https://www.lego.com/en-us/mindstorms/downloads/download-software

There is also a lightweight version of that program available for iPad and Android tablets:<br>
https://www.lego.com/en-us/mindstorms/apps/ev3-programmer-app

Block based languages are a great way to get started, but at some point in your programming journey, it's time to move
away from block based languages (like Scratch) and move into the more traditional text-based programming languages.
One of the best, first languages to learn is Python. Using the Lego EV3 with Python can be a lot of fun and it can help
motivate learning.  There are really only 2 factors limiting more schools from using EV3 + Python.
- Costs (sorry can't help you with that one)
- Technical challenges (that we can help with)

Indeed it takes someone with a bit of tech savvy to get started, but there are a lot of great tools to help.
This repository uses some of those great tools and tries to provide examples and links to use them.

First we start with the operating system on the EV3 programming brick.  Instead of using the default operating system
that ships with the EV3 from Lego we'll dual boot using an SD card. The new os is called **ev3dev** and it's based on Linux.<br>
http://www.ev3dev.org/

ev3dev can use many different programming languages, not just Python. We only care about Python though.  In
order to use Python we need to leverage a Python library, so that we have commands to communicate the the motors and 
sensors on the board.  The built-in Python library that ships with ev3dev is called python-ev3dev.<br>
Github: https://github.com/rhempel/ev3dev-lang-python
<br>
Documentation: http://python-ev3dev.readthedocs.io/en/latest/

In order to use ev3dev with read the Getting Started page on ev3dev.org.<br>
http://www.ev3dev.org/docs/getting-started/

Then for the robots we use at Rose-Hulman I did some additional customizations. Starting in 2016 we built a fleet of 10
EV3 robots to use in our CSSE120 Introduction to Programming course at Rose-Hulman. Here is a different doc which
documents some Rose-Hulman specific work and our customizations.<br>
https://docs.google.com/document/d/1jNlT9JKff3p9TyrDQwF3XjakaLEp_ilD1wNaHr7c67o/edit?usp=sharing

Once you have your robot setup and rockin you need material to teach students how to use the robot.  That is where
this repository begins.

## What is in this repository

This repository is broken into different folders that each have a different purpose:
- `examples` - Finished examples that can be run to demo different robot features. Reference the code in this folder when doing your own work. 
- `libs` - A special folder that will contain modules that are available to all other modules. Students will be given an mqtt module and will be expected to build their own robot controller module.
- `sandbox` - This folder has 5 subfolders that all start out identical.  Each identical subfolder is for 1 team member to work individually while learning ev3dev and while doing initial development in a contained environment for their work.
- `project` - This folder is for the course final project code.  Modules can be moved from the sandbox into this folder and work and be integrated into a single combined project.

## Getting started

To get started with this tutorial you need upload the code into a folder on EV3.  Since this
repository is for csse120 you need to make sure to push the code onto the EV3 into the folder
/home/robot/csse120.  That folder path is only important for the libs folder which must be at the folder path /home/robot/csse120/libs.  If you
don't care about the libs folder then put the code anywhere you like. :)

Once uploaded to your EV3 try some of the example programs, then start working the TODOs in a sandbox folder.
We recommend you use PyCharm Professional (not PyCharm Edu).  University students can get
a free copy of PyCharm Professional.   https://www.jetbrains.com/student/

To setup PyCharm Professional with EV# visit this tutorial.
http://www.ev3dev.org/docs/tutorials/setting-up-python-pycharm/#additional-features-for-the-pycharm-professional-version
