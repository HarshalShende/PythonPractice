import turtle
from turtle import*

#screen for output
screen = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()
speed(0)


# initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()

# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(83.5)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(83.5)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(83.5)
t.left(90)
t.forward(400)
t.left(90)
t.forward(83.5)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(35, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(-28.5, -4)
t.pendown()
t.color("navy")
for i in range(24):
	t.begin_fill()
	t.circle(1.5)
	t.end_fill()
	t.penup()
	t.forward(7.5)
	t.right(15)
	t.pendown()
	
# Small Blue Circle
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
# Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
	t.forward(30)
	t.backward(30)
	t.left(15)

t.penup()
t.goto(-200, 250)
t.pendown()
t.color('blue')
t.write('जय हिंद', font=("Broadway", 70, "bold"))

t.penup()
t.goto(-400, -400)
t.pendown()
t.color('blue')
t.write('India In Olympics', font=("Broadway", 80, "bold"))


	
#to hold the
#output window
turtle.done()
