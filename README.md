# PA1473 - Software Development: Agile Project Group 10

## Introduction

This is a repository guiding you through our project developing software for the LEGO® MINDSTORMS EV3 Robot Arm H25. In short the robot can sort different packages by the colors blue, green, yellow or red.

## Getting started

This section is supposed to guide a new developer through the steps of how to set up the project and install the deppendencies they need to start developing.
If not already done: -Install Github desktop from https://desktop.github.com/
Create a Github account at https://github.com/
Create a Trello account and  https://trello.com/b/ldWZupD6/scrum-board
Install Python programming language
In CMD do commands as administrator:
    pip install pybricks
Install Visual Studio Code (VSCode)
Install VSCode extention LEGO Mindstorms EV3 MicroPython
Clone the projects repository (if you are interested) from https://github.com/Leo4-g/ev3-Assignement

## Building and running

The robot begins by performing a calibration sequence in which it modifies the arm's angles, positions the base motor, and establishes the claw's operational range. After finishing the setup process, it starts picking up things from the default pickup zone (on the right) and analyzing their colors. Then, according to their hue, it moves the objects to the following zones: Left for Blue, Middle Left for Yellow, Middle for Red, and Middle Right for Green. There is no end to this process.  
 
The robot recognizes when there are no things in the pickup zone and, upon receiving notification, makes repeated attempts to successfully recover an object. The terminal displays a menu when the pause button (UP) is pressed, enabling modification of parameters such zone settings and pickup/drop height. 
 
Users can also create a report that shows how many blocks of various colors were moved during a session.  
 
Each function, which may be accessed by buttons on the robot, prints instructions on the terminal interface. The robot has an emergency button on its console that, when hit, allows it to stop working on its present duty immediately and shut down safely. 

## Features

This is the user stories completed in this project:

- [x] US_1: As a customer, I want the robot to pick up items from a designated position.
- [x] US_2: As a customer, I want the robot to drop items off at a designated position.
- [x] US_3: As a customer, I want the robot to be able to determine if an item is present at a given location.
- [x] US_4: As a customer, I want the robot to tell me the color of an item at a designated position.
- [x] US_5: As a customer, I want the robot to drop items off at different locations based on the color of the item.
- [x] US_6: As a customer, I want the robot to be able to pick up items from elevated positions.
- [x] US_8: As a customer, I want to be able to calibrate items with three different colors and drop the items off at specific drop-off zones based on color.
- [x] US_9: As a customer, I want the robot to check the pickup location.
- [ ] US_10: As a customer, I want the robots to sort items at a specific time.
- [ ] US_11: As a customer, I want two robots (from two teams) to communicate and work together on items sorting without colliding with each other.
- [ ] US_12: As a customer, I want to be able to manually set the locations and heights of one pick-up zone and two drop-off zones.
- [x] US_13: As a customer, I want to easily reprogram the pickup and drop off zone of the robot.
- [ ] US_14: 
- [x] US_15: As a customer, I want to have an emergency stop button, that immediately terminates the operation of the robot safely.
- [x] US_16: As a customer, I want the robot to be able to pick an item up and put it in the designated drop-off location within 5 seconds.
- [ ] US_17: As a costumer, I want the robot to pick up items from a rolling belt and put them in the designated positions based on color and shape.
- [x] US_18: As a customer, I want to have a pause button that pauses the robot`s operation when the button is pushed and then resumes the program from the same point when I push the button again.
- [ ] US_19: As a costumer, I want a very nice dashboard to configure the robot program and start some tasks on demand.

## Contributors

Vincent Jyrell
Arvid Qvarnström
Miguel Ramos
Leo Ghaffari
Isak Svenningsson
