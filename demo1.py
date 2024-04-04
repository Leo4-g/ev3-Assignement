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

positions = [180,135,90,-10,0]
elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)

def startup():
    ev3.screen.print("Starting")
    gotoposition(30)
    setbaseposition()


def finished():
    gotoendposition()
    ev3.screen.print("Finished")
    ev3.speaker.say("goodbye")


def setbaseposition():
    ev3.screen.print("SETTING BASE POSITION...")
    elbowup()
    base_motor.run(-60)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    wait(1000)
    base_motor.reset_angle(0)

    ev3.screen.print("BASE POSITION FOUND")


def gotoendposition():
    elbowup()
    gotoposition(45)
    elbowdown()


def gotoposition(pos):
    elbowup()
    base_motor.run_target(90, pos)


def pickupposition(pos):

    elbowup()
    base_motor.run_target(90, pos)


def closegrip():  
    ev3.screen.print("CLOSE GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
     

def opengrip():
    ev3.screen.print("OPEN GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)


def elbowup():
    ev3.screen.print("ELBOW UP")
    elbow_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=50)
    elbow_motor.reset_angle(90) 


def elbowdown():
    ev3.screen.print("ELBOW DOWN")
    elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=25)
   

def pickup(pos):
    ev3.screen.print("PICK UP")

    pickupposition(pos) 

    opengrip()
    elbowdown()
    closegrip()


def dropoff(position):
    gotoposition(position)
    elbowdown()
    opengrip()
    elbowup()


def run():
    startup()
    pickup(positions[3])

    dropoff(positions[0])
    finished()

run()

