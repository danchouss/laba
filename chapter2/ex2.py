
import turtle as tr
from random import *

tr.speed(5)
num = [0] * 10
num[0]=[(100, 90), (200, 90), (100, 90), (200, 270)]
num[4]=[(0, 90), (100, 270), (100, 270), (100, 180), (100, 90), (100, 270), (100,180), (200, 270)]
num[7]=[(100, 180), (100, 225), (100*(2**0.5), 45), (100, 180), (100, 315), (100*(2**0.5), 315) ]
num[1]=[(0, 45), (100*2**0.5, 180), (100*2**0.5, 225), (200, 180), (200, 270)]
def tsifra(x):
    tr.left(180)
    for step, rot in num[x]:
        tr.forward(step)
        tr.left(rot)
    tr.penup()
    tr.forward(200)
    tr.pendown()

tsifra(1)
tsifra(4)
tsifra(1)
tsifra(7)
tsifra(0)
tsifra(0)

