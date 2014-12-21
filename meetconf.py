import turtle
turtle.speed(0)
turtle.pu()
turtle.pensize(5)
pensize=5
def paint (x,y):
	#starting the P
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x,y+20)
	turtle.goto(x+20,y+20)
	turtle.goto(x+20,y+10)
	turtle.goto(x,y+10)
	turtle.pu()
	#starting the A
	turtle.goto(x+60,y)
	turtle.pd()
	turtle.goto(x+80,y+20)
	turtle.goto(x+100,y)
	turtle.pu()
	turtle.goto(x+75,y+10)
	turtle.pd()
	turtle.goto(x+85,y+10)	
	turtle.pu()
	#starting the I
	turtle.goto(x+140,y+20)
	turtle.pd()
	turtle.goto(x+140,y)
	turtle.pu()
	#starting the N
	turtle.goto(x+180,y)
	turtle.pd()
	turtle.goto(x+180,y+20)
	turtle.goto(x+200,y)
	turtle.goto(x+200,y+20)
	turtle.pu()
	#starting the T
	turtle.goto(x+240,y+20)
	turtle.pd()
	turtle.goto(x+260,y+20)
	turtle.pu()
	turtle.goto(x+250,y+20)
	turtle.pd()
	turtle.goto(x+250,y)
	turtle.pu()

paint (-250,325)

turtle.goto(0,0)
turtle.pd()
turtle.speed(9)

turtle.onscreenclick(turtle.goto,btn=1,add=True)
turtle.ondrag(turtle.goto,btn=1,add=True)

#defining basic actions
def keys():
	turtle.clear()
	turtle.speed(0)
	turtle.pencolor("black")
	turtle.pu()
	paint (-250,325)
	turtle.goto(0,0)
	turtle.pd()
	turtle.speed(9)
	pensize=5
turtle.getscreen().onkeypress(keys,"space")
turtle.getscreen().listen()

def keys2():
	turtle.pu()
turtle.getscreen().onkeypress(keys2,"f")
turtle.getscreen().listen()

def keys3():
	turtle.pd()
turtle.getscreen().onkeypress(keys3,"d")
turtle.getscreen().listen()

#defining colors
def black():
	turtle.pencolor("black")
turtle.getscreen().onkeypress(black,"p")
turtle.getscreen().listen()

def red():
	turtle.pencolor("red")
turtle.getscreen().onkeypress(red,"q")
turtle.getscreen().listen()

def orange():
	turtle.pencolor("orange")
turtle.getscreen().onkeypress(orange,"w")
turtle.getscreen().listen()

def yellow():
	turtle.pencolor("yellow")
turtle.getscreen().onkeypress(yellow,"e")
turtle.getscreen().listen()

def green():
	turtle.pencolor("green")
turtle.getscreen().onkeypress(green,"r")
turtle.getscreen().listen()

def lightblue():
	turtle.pencolor("light blue")
turtle.getscreen().onkeypress(lightblue,"t")
turtle.getscreen().listen()

def blue():
	turtle.pencolor("blue")
turtle.getscreen().onkeypress(blue,"y")
turtle.getscreen().listen()

def purple():
	turtle.pencolor("purple")
turtle.getscreen().onkeypress(purple,"u")
turtle.getscreen().listen()

def pink():
	turtle.pencolor("pink")
turtle.getscreen().onkeypress(pink,"i")
turtle.getscreen().listen()

def fuchsia():
	turtle.pencolor("fuchsia")
turtle.getscreen().onkeypress(fuchsia,"o")
turtle.getscreen().listen()
	
#defining shapes
def circle():
	turtle.shape("circle")
turtle.getscreen().onkeypress(circle,"s")
turtle.getscreen().listen()
#the problem is that the line itself isnt a circle and i cant change shapes after a circle


turtle.mainloop()
