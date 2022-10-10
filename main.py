#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import random as rand
import math

ev3 = EV3Brick()

def wait_for_button(ev3):
    pressed = []

    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()

    button = pressed[0]

    while any(ev3.buttons.pressed()):
        pass

    return button

x = 178/2
y = 128/2
r = 10
fill = True
color = Color.BLACK

ingame = True

circles = []

class Circle:
    def __init__(self, x, y, r, fill):
        self.x = x
        self.y = y
        self.r = r

        self.fill = fill
        self.color = Color.BLACK

player = Circle(x, y, r, True)

def RandomCircle():
    rR = rand.randint(player.r-8, player.r+2)
    rX = rand.randint(0+rR, 178-rR)
    rY = rand.randint(0+rR, 128-rR)

    rCircle = Circle(rX, rY, rR, False)

    return rCircle


while ingame:
    ev3.screen.draw_circle(player.x, player.y, player.r, player.fill, player.color)

    if len(circles) < 5:
        for _ in range(5 - len(circles)):
            c = RandomCircle()
            circles.append(c)

    for i in circles:
        ev3.screen.draw_circle(i.x, i.y, i.r, i.fill, i.color)

    for circle in circles:
        if ((player.x - circle.x <= 10) and (player.x - circle.x > 0) or (circle.x - player.x <= 10) and (circle.x - player.x > 0)) and ((player.y - circle.y <= 10) and (player.y - circle.y > 0) or (circle.y - player.y <= 10) and (circle.y - player.y > 0)):
            if circle.r <= player.r:
                circles.remove(circle)
                player.r = player.r + circle.r/4
            elif circle.r > player.r:
                print('vege')
                break

    button = wait_for_button(ev3)

    if button == Button.LEFT:
        player.x = player.x - 10
    elif button == Button.RIGHT:
        player.x = player.x + 10
    elif button == Button.UP:
        player.y = player.y - 10
    elif button == Button.DOWN:
        player.y = player.y + 10

    ev3.screen.clear()
