# Solution: Draw a Star (Week 11, Programming Problem 2)

import turtle

t = turtle.Turtle()
t.speed(3)
t.color("red")

for _ in range(5):
    t.forward(150)
    t.right(144)   # exterior angle of a 5-pointed star

turtle.done()
