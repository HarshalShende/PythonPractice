#by Derek Vidovic
#This was an attempt to make a small shooting game in Python
#that would involve very long, slow-moving bullets.
#The speed of Python/turtle makes this currently impossible.

from turtle import *
from random import *

class Bullet:    
    def __init__(self, x, y, heading, length=100, r=1, v=10):
        self.length = length
        self.v = v
        self.t = Turtle()
        self.t.penup()
        self.t.speed(0)
        self.t.setx(x)
        self.t.sety(y)
        self.t.pensize(r)
        self.t.setheading(heading)
        self.t.pendown()

    def update(self, timeChange):
        """Draws more of the bullet's path if the bullet is still traveling.
        Otherwise, clears the bullet's path. Returns None if the caller
        should continue updating the bullet. Otherwise, returns a Turtle
        for re-use."""
        #self.t.speed(1)#DEBUG
        if self.length <= 0:
            self.t.clear()
            self.t.hideturtle()
            return self.t
        toDraw = self.v * timeChange
        if toDraw > self.length:
            toDraw = self.length
        self.t.fd(toDraw)
        self.length -= toDraw
        return None


class Gun:
    """Represented by a rectangle. Fires bullets.
    Width is MIN_WIDTH + caliber; length is MIN_LENGTH + range/3."""
    MIN_WIDTH = 5
    MIN_HEIGHT = 10
    
    def __init__(self, x, y, heading=0, ammo=1, dist=100, caliber=1, v=10):
        self.x = x
        self.y = y
        self.heading = heading
        self.dist = dist
        self.caliber = caliber
        self.t = Turtle()
        #TODO

    def draw(self):
        self.t.pu()
        self.t.setx(self.x)
        self.t.sety(self.y)

    def redraw(self):
        for i in range(4):
            self.t.undo()
        self.draw()

#runs the program
def run():
    bullets = []
    for i in range(25):
        bullets.append(Bullet(100, 100, heading=randint(0,359), v=randint(5,50),
                              length=randint(50,500)))
##    Bullet(100,100,heading=0), Bullet(100,100,heading=90,v=1),
##               Bullet(100,100,heading=0, length=1000), Bullet(100,100,heading=100, v=2)]
    for i in range(100):
        for t in bullets:
            t.update(1)
run()
