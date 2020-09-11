import turtle

i=0

while i<10:
	turtle.shape('turtle')
	turtle.forward(50+i*20)
	turtle.left(90)
	turtle.forward(50+i*20)
	turtle.left(90)
	turtle.forward(50+i*20)
	turtle.left(90)
	turtle.forward(50+i*20)
	turtle.penup()
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(10)
	turtle.left(180)
	turtle.pendown()
	i+=1
 
	


