import turtle as tr

n=int(input())
i=1
while i<=n:
	tr.shape('turtle')
	tr.width(3)
	x=360/n
	tr.right(x*i)
	tr.forward(100)
	tr.stamp()
	tr.right(180)
	tr.forward(100)
	tr.right(180-x*i)
	i+=1

	



