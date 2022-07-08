import turtle
from turtle import*

# object tr for turtle
t= turtle.Turtle()

# set pen size value
t.pensize(15)



t.color("blue")
t.penup()
t.goto(-220, 100)
t.pendown()
t.circle(90)

t.color("black")
t.penup()
t.goto(0, 100)
t.pendown()
t.circle(90)

t.color("red")
t.penup()
t.goto(220, 100)
t.pendown()
t.circle(90)

t.color("yellow")
t.penup()
t.goto(-110, 10)
t.pendown()
t.circle(90)

t.color("green")
t.penup()
t.goto(110, 10)
t.pendown()
t.circle(90)



t.penup()
t.goto(-180, -180)
t.pendown()
t.color('blue')
t.write('Tokyo', font=("Broadway", 80, "bold"))

t.penup()
t.goto(-270, -280)
t.pendown()
t.color('blue')
t.write('Olympics', font=("Broadway", 80, "bold"))




