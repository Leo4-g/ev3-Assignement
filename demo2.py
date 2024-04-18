#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.parameters import Color, SoundFile
from pybricks.tools import wait


# Initialize the EV3 Brick
ev3 = EV3Brick()

gripper_motor = Motor(Port.A)

elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

touch_sensor = TouchSensor(Port.S1)

color_sensor = ColorSensor(Port.S2)

#positions = [177,135,82,-15]
positions = [180,140,90,0]
colors = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN]
elbow_motor.control.limits(speed=150, acceleration=150)
base_motor.control.limits(speed=150, acceleration=150)

def startup():
    ev3.screen.print("Starting")
    elbowdown()
    gotoposition(30)
    setbaseposition()

def finished():
    gotoendposition()
    ev3.screen.print("Finished")
    ev3.speaker.say("I am finished goodbye")

#sätt nollpunkt när roboten har tryckt in knappen
def setbaseposition():
    ev3.screen.print("SETTING BASE POSITION...")
    #elbowup()
    base_motor.run(-60)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    wait(200)
    base_motor.reset_angle(0)

    ev3.screen.print("BASE POSITION FOUND")


def gotoendposition():
    ev3.speaker.say("going back to start position")
    elbowup()
    base_motor.run_target(60, 38)
    elbowdown()


def gotoposition(pos):
    elbowup()
    base_motor.run_target(60, pos)


def pickupposition(pos):
    #elbowup()
    base_motor.run_target(90, pos)


def closegrip():  
    ev3.screen.print("CLOSE GRIP")
    gripper_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=50)
     


def opengrip():
    ev3.screen.print("OPEN GRIP")
    gripper_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(300, -90)


def elbowup():
    ev3.screen.print("ELBOW UP")
    elbow_motor.run_target(50, 45, then=Stop.HOLD)
   # elbow_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=50)
    elbow_motor.reset_angle(0)


def elbowdown():
    ev3.screen.print("ELBOW DOWN")
    elbow_motor.run_target(50, -45, then=Stop.COAST)

    #elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=25)


def checkcolor():
    Colorfound = False
    ev3.speaker.say("Will check color")
    elbow_motor.reset_angle(0)
    elbow_motor.run_target(50, 45)
    wait(500)

    while Colorfound == False:
        # Read the raw RGB values
        measuredcolor = color_sensor.color()

        if measuredcolor in colors:
            if measuredcolor == Color.BLUE:
                ev3.speaker.say("blue")
                ev3.screen.print("BLUE COLOR")
            elif measuredcolor == Color.RED:
                ev3.speaker.say("red")
                ev3.screen.print("RED COLOR")
            elif measuredcolor == Color.GREEN:
                ev3.speaker.say("green")
                ev3.screen.print("GREEN COLOR")
            elif measuredcolor == Color.YELLOW:
                ev3.speaker.say("yellow")
                ev3.screen.print("YELLOW COLOR")

            Colorfound = True
    return measuredcolor


def pickup(pos,cc):
    ev3.screen.print("PICK UP")
    ev3.speaker.say("Arvid will pick up the object")

    pickupposition(pos) 

    opengrip()
    elbowdown()
    closegrip()
    if cc is True:
        color = checkcolor()
    ev3.speaker.beep()
    if cc is True:
        return color


def dropoff(position, color, dropcolorspecial):
    if dropcolorspecial == True:    
        if color == Color.BLUE:
            position = positions[0]
        if color == Color.RED:
            position = positions[1]
        if color == Color.GREEN:
            position = positions[2]
        if color == Color.YELLOW:
            position = positions[3]
    gotoposition(position)
    elbowdown()
    opengrip()


def runtest():
    checkcolor=True
    dropcolorspecial=True
    startup()

    mycolor = pickup(positions[3], checkcolor)
    
    dropoff(positions[0], mycolor, dropcolorspecial)
    #elevated_dropoff(positions[2], 0)
    finished()

runtest()

#elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=25)

#elbow_motor.run_target(50, -45, then=Stop.HOLD)