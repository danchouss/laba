import turtle as tr
from random import *

i=0

while i<1000:
    tr.shape('turtle')
    tr.forward(randint(1, 50))
    x=randint(1, 2)
    if x==1:
        tr.left(randint(1, 360))
    if x==2:
        tr.right(randint(0, 360))
    i+=1
