#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random

ev3 = EV3Brick()


def wait_for_button(ev3):
    pressed = []

    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()

    button = pressed[0]

    while any(ev3.buttons.pressed()):
        pass

    return button


szam = random.randint(1, 20)
guess = 0
answer = 0
maxGuesses = 5
ev3.screen.print("Gondoltam egy\nszamra 1 es 20\nkozott!")
wait_for_button(ev3)
currentGuess = 0

while answer != szam:
    ev3.screen.clear()
    ev3.screen.print("Probak: " + str(maxGuesses-currentGuess))
    if answer < szam:
        ev3.screen.print("Nagyobb")
    elif answer > szam:
        ev3.screen.print("Kisebb")
    ev3.screen.draw_text(ev3.screen.width/2, ev3.screen.height/2, guess, Color.BLACK)

    button = wait_for_button(ev3)

    if button == Button.UP:
        guess = guess + 1
    elif button == Button.DOWN:
        guess = guess - 1
    elif button == Button.CENTER:
        answer = guess
        currentGuess = currentGuess + 1

    if currentGuess == maxGuesses:
        break


ev3.screen.clear()
if currentGuess == maxGuesses:
    ev3.screen.print("Kifogytal a \nprobalkozasokbol!")
else:
    ev3.screen.print("Gratulalok,\nkitalaltad!\n" + str(szam))

wait_for_button(ev3)
