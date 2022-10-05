#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

ev3 = EV3Brick()

posX = 178/2
posY = 118
r = 10
fill = True
color = Color.BLACK

ingame = True

def Circle(x,y,r,fill,color):
    ev3.screen.draw_circle(x,y,r,fill,color)

Circle(posX, posY, r, fill, color)

while ingame:
    if Button.LEFT in ev3.buttons.pressed():
        posX = posX - 0.1
    
    if Button.RIGHT in ev3.buttons.pressed():
        posX = posX + 0.1

    ev3.screen.clear()
    Circle(posX, posY, r, fill, color)
