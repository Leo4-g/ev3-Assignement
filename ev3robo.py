#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from time import sleep
import sys

#Initialize the EV3 Brick
ev3 = EV3Brick()
gripper_motor = Motor(Port.A)
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
elbow_motor.control.limits(speed=120, acceleration=100)
base_motor.control.limits(speed=120, acceleration=100)
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)

MENU_PICK_DROP ="""
UP: PICK UP
DOWN: DROP OFF"""

MENU_BLOCK ="""
LEFT = 2 Blocks
CENTER = 1 Block
DOWN = 0 Blocks
"""

MENUTEXT_COLOR ="""
UP: BLUE
LEFT: YELLOW
RIGHT: RED
DOWN: GREEN
CENTER: PICK-UP
"""
MENUTEXT_DROPZONES = """
UP: MIDDLE_LEFT
LEFT: LEFT
RIGHT: RIGHT
DOWN: MIDDLE_RIGHT
CENTER: MIDDLE
"""
PAUSE_MENU = """
CENTER: PICK/DROP
DOWN: RESUME
RIGHT: CHANGE ZONE
LEFT: COUNT
"""
#Positions
DROPZONES = [206, 159, 113, 66, 8]

#Starting position
elbow_motor.run_target(60, 5)
elbow_motor.run_time(-30, 2000)
elbow_motor.run(15)
#Detecting height of color sensor
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)
while color_sensor.reflection() > 0:
    wait(10)
elbow_motor.reset_angle(0)
elbow_motor.hold()

#Setting base position
base_motor.run(-60)
while not touch_sensor.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()

#Setting base position for grip
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(1000, -20)
gripper_motor.run_target(200, -90)
ev3.speaker.say("Starting")

a = True
pickup_zone = DROPZONES[4]
Blue = "Blue"
Red = "Red"
Yellow = "Yellow"
Green = "Green"
Blank = ""
pickup_height = [33]
drop_height = [33]
count_blue = 0
count_yellow = 0
count_red = 0  
count_green = 0

'''
def change_drop_pick():
    #global pickup_height
    #global drop_height

    #print(MENU_PICK_DROP)
    #while True:
        #wait(1000)
        #if Button.UP in ev3.buttons.pressed():
         #   print(MENU_BLOCK)
          #  while True:
          #      wait(1000)
          #      if Button.LEFT in ev3.buttons.pressed():
           #         pickup_height[0] = 15
            #        return 
             #   elif Button.CENTER in ev3.buttons.pressed():
              #      pickup_height[0] = 22
               #     return 
                #elif Button.DOWN in ev3.buttons.pressed():
                 #   pickup_height[0] = 33
                  #  return 
            elif Button.DOWN in ev3.buttons.pressed():
            print(MENU_BLOCK)
            while True:
                wait(1000)
                if Button.LEFT in ev3.buttons.pressed():
                    drop_height[0] = 15
                    return drop_height
                elif Button.CENTER in ev3.buttons.pressed():
                    drop_height[0]= 22
                    return drop_height
                elif Button.DOWN in ev3.buttons.pressed():
                    drop_height[0] = 33
                    return '''


def choose_color():
    print("choose a color")
    print(MENUTEXT_COLOR)
    while True:
        wait(1000)
        if Button.UP in ev3.buttons.pressed():
            return 0
        elif Button.LEFT in ev3.buttons.pressed():
            return 1
        elif Button.RIGHT in ev3.buttons.pressed():
            return 2
        elif Button.DOWN in ev3.buttons.pressed():
            return 3
        elif Button.CENTER in ev3.buttons.pressed():
            return 4
    
def change_zone():
    color_id = choose_color()
    print("choose a zone")
    print(MENUTEXT_DROPZONES)
    while True:
        wait(1000)
        if Button.UP in ev3.buttons.pressed():
            DROPZONES[color_id] = 159
            return DROPZONES
        elif Button.LEFT in ev3.buttons.pressed():
            DROPZONES[color_id] = 206
            return DROPZONES
        elif Button.RIGHT in ev3.buttons.pressed():
            DROPZONES[color_id] = 8
            return DROPZONES
        elif Button.DOWN in ev3.buttons.pressed():
            DROPZONES[color_id] = 66
            return DROPZONES
        elif Button.CENTER in ev3.buttons.pressed():
            DROPZONES[color_id] = 113
            return DROPZONES
        print(DROPZONES)
        
        



def pause():    
    print("Pausing")
    print(PAUSE_MENU)
    base_motor.hold()
    elbow_motor.hold()
    gripper_motor.hold()
    elbow_motor.hold()
    while True:
        wait(1) 
        if Button.RIGHT in ev3.buttons.pressed():
            change_zone()
            print("ZONE CHANGED")
            print(DROPZONES) 
            print(PAUSE_MENU)
        elif Button.LEFT in ev3.buttons.pressed():
            print("BLUE Cubes: ", count_blue, '\n', "Yellow Cubes: ", count_yellow, "\n", "Red Cubes: ", count_red, "\n", "Green Cubes: ", count_green)
            wait(3000)
            print(PAUSE_MENU)
        #elif Button.CENTER in ev3.buttons.pressed():
            #change_drop_pick()
           # print(PAUSE_MENU)
        elif Button.DOWN in ev3.buttons.pressed():
            print(DROPZONES)
            print(pickup_height)
            print(drop_height)
            print("Resuming")
            wait (500)
            return

        

def emergency():
    print("emergency stop")
    elbow_motor.run_target(10, -drop_height[0])
    gripper_motor.run_target(100, -90)
    base_motor.hold()
    elbow_motor.hold()
    gripper_motor.hold()
    elbow_motor.hold()
    print("program stopped")
    sys.exit()


def robot_pickup(position):
    if Button.UP in ev3.buttons.pressed():
        pause()
    elif Button.CENTER in ev3.buttons.pressed():
        emergency() 
 
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -pickup_height[0])
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    elbow_motor.run_target(60, 0)



def robot_dropoff(position):
    if Button.UP in ev3.buttons.pressed():
        pause()
    elif Button.CENTER in ev3.buttons.pressed():
        emergency()

    
    speed = 200

    while base_motor.angle() != position:
        if Button.UP in ev3.buttons.pressed():
            pause()
        elif Button.CENTER in ev3.buttons.pressed():
            emergency()

        if base_motor.angle() < position:
            base_motor.run(speed)
        else:
            base_motor.run(-speed)

    base_motor.stop()
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -drop_height[0])
    gripper_motor.run_target(200, -90)
    elbow_motor.run_target(60, 0)

def rgb_value():
    if ev3.buttons.pressed():
        pause()
    color_value = color_sensor.rgb()
    print(color_value)
    return color_value

def check_angle():
    isblock = False
    angle=(gripper_motor.angle())
    ev3.screen.print(str(angle))

    if angle<-20:
        print("The motor is holding a block.")
        isblock = True
    
    else:
        print("The motor is not holding a block.")
    wait(200)
    return isblock


def check_if_present():
    isblock = False
    while isblock == False:
        isblock = check_angle()
    return False

def check_color(rgb):

    if Button.UP in ev3.buttons.pressed():
        pause()
    elif Button.CENTER in ev3.buttons.pressed():
        emergency()  
    red, green, blue = rgb
    #We do not want to divide by zero.
    if green == 0:
        green = 1
    if blue == 0:
        blue = 1
    if red == 0:
        red = 1
    

    

    rg_ratio = red / green
    rb_ratio = red / blue
    gr_ratio = green / red
    gb_ratio = green / blue
    br_ratio = blue / red
    bg_ratio = blue / green

    if check_angle() == False:
        color = "The motor is not holding a block."
        gripper_motor.run_target(200, -90)
    elif  rg_ratio >= 1 and rb_ratio > 1 and gr_ratio <= 1 and gb_ratio >= 1 and br_ratio <= 1 and bg_ratio <= 1:
        color = "Yellow"
    elif  rg_ratio >= 2 and rb_ratio >= 1.5 and gr_ratio <= 1 and br_ratio <= 1:
        color = "Red"
    elif  rg_ratio <= 1 and rb_ratio <= 1 and gr_ratio >= 1 and gb_ratio >0.8  and br_ratio >= 1 and bg_ratio < 1.2:
        color = "Green"
    elif  rg_ratio <= 1 and rb_ratio < 1 and gr_ratio >= 1 and gb_ratio < 1 and br_ratio > 1 and bg_ratio > 1:
        color = "Blue"
   

    print(color)
    ev3.speaker.say(color)
    return color






while a == True:
    value = DROPZONES[4]
    robot_pickup(value)

    rgb = rgb_value()

    color_name = check_color(rgb)

    if ev3.buttons.pressed():
        pause()


    if color_name == Blue:
        count_blue = count_blue + 1
        value = DROPZONES[0]
        robot_dropoff(DROPZONES[0])

    elif color_name == Yellow:
        count_yellow = count_yellow + 1
        value = DROPZONES[1]
        robot_dropoff(value)

    elif color_name == Red:
        count_red = count_red + 1
        value = DROPZONES[2]
        robot_dropoff(value)

    elif color_name == Green:
        count_green = count_green + 1
        value = DROPZONES[3]
        robot_dropoff(value)