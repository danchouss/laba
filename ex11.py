import math

t.speed(100)
t.left(90)




def funcss(vs):
    i=0
    j=0
    while i<360:
        t.shape('turtle')
        t.forward(vs)
        t.left(1)
        i+=1
        if i==359:
            while j<360:
                t.shape('turtle')
                t.forward(vs)
                t.right(1)
                j+=1
x=1
while x<10:
    funcss(x)
    x+=1
