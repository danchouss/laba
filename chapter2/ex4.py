import turtle as tr
from random import *

tr.speed(10)
number_of_turtles = 42

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.shapesize(0.5, 0.5)
    unit.goto(randint(-250, 250), randint(-250, 250))
    unit.speed(randint(1, 10))
    unit.seth(randint(0,360))

while True:
    for unit in pool:
        if abs(unit.xcor())>250:
            unit.seth(180-unit.heading())
        if abs(unit.ycor())>250:
            unit.seth(360-unit.heading())
        unit.fd(unit.speed()*0.5)
