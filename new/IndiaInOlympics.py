import turtle
from turtle import*

# object tr for turtle
t= turtle.Turtle()



#set pensize for flag
t.pensize(2)
# initially penup()
t.penup()
t.goto(-200, 100)
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
t.goto(35, -25)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, -25)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(-28.5, -29)
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
t.goto(10, -25)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
# Spokes
t.penup()
t.goto(0, -25)
t.pendown()
t.pensize(2)
for i in range(24):
	t.forward(29)
	t.backward(29)
	t.left(15)



# set pen size value
t.pensize(13)

t.color("blue")
t.penup()
t.goto(-220, 210)
t.pendown()
t.circle(90)

t.color("black")
t.penup()
t.goto(0, 210)
t.pendown()
t.circle(90)

t.color("red")
t.penup()
t.goto(220, 210)
t.pendown()
t.circle(90)

t.color("yellow")
t.penup()
t.goto(-110, 120)
t.pendown()
t.circle(90)

t.color("green")
t.penup()
t.goto(110, 120)
t.pendown()
t.circle(90)



t.penup()
t.goto(-500, -100)
t.pendown()
t.color('orange')
t.write('Jai', font=("Bodoni MT Black", 90, "bold"))

t.penup()
t.goto(300, -100)
t.pendown()
t.color('green')
t.write('Hind', font=("Bodoni MT Black", 90, "bold"))


t.penup()
t.goto(-700, -340)
t.pendown()
t.color('blue')
t.write('India In Olympics', font=("Rockwell Extra Bold", 100, "bold"))




