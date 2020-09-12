import turtle as t
import math

t.speed(100)

i=0
while i<360:
    if i==359:
        i=0
        t.left(45)
    t.shape('turtle')
    t.forward(1)
    t.left(1)
    i+=1
