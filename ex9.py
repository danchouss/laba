import turtle as t
import math
x=1
t.speed(10)
t.shape('turtle')
n=3
R=30
t.penup()
t.goto(R,0)
t.pendown()

def risovach(x):
    while x<=n:	
        t.left((180- 360/n)/2)
        t.left(360/n)
        t.forward(2*R*math.sin(math.pi/n))
        t.right((180-360/n)/2)
        x+=1

while n<=11:
    risovach(x)
    n+=1
    R+=20
    t.penup()
    t.goto(R,0)
    t.pendown()

