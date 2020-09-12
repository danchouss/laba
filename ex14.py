import turtle as t
t.shape('turtle')
def patrick(n):
    t.left(180 - (180 / n))
    t.forward(200)
x=1
n=5
while x <= n:
    patrick(n)
    x += 1
    if(x>n):
        t.up()
        t.goto(200, 30)
        t.down()
        n=11
        x=0
        while x <= n:
            patrick(n)
            x += 1
