import turtle as tr
from random import *

dt=1
Vx=40
Vy=40
x=0
ay=-10
y=0
while dt<1000:
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    tr.goto(x, y)
    dt+=0.01
