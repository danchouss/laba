import turtle as tr
from random import *

num = [0] * 10
num[0]=[(100, 90), (200, 90), (100, 90), (200, 90), (100, 0)]
num[4]=[(0, 90), (100, 270), (100, 270), (100, 180), (200, 180), (200, 90)]
num[7]=[(100, 135), (100*(2**0.5), 315), (100, 270)]
num[1]=[(0, 315), (100*2**0.5, 135), (200, 180), (200, 90)]
def tsifra(x):
    if x==1:
        tr.penup()
        tr.right(90)
        tr.forward(100)
        tr.left(90)
        tr.pendown()
        for step, rot in num[x]:
            tr.forward(step)
            tr.right(rot)
    else:
        for step, rot in num[x]:
            tr.forward(step)
            tr.right(rot)
    if x==7:
        tr.penup()
        tr.forward(100)
        tr.left(90)
        tr.forward(200)
        tr.right(90)
        tr.pendown()
    tr.penup()
    tr.forward(100)
    tr.pendown()

tsifra(1)
tsifra(4)
tsifra(1)
tsifra(7)
tsifra(0)
tsifra(0)

