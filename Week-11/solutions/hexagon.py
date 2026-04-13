# Solution: Draw a Hexagon (Week 11, Programming Problem 1)

import turtle

t = turtle.Turtle()
t.speed(3)

for _ in range(6):
    t.forward(100)
    t.right(60)   # 360 / 6 = 60 degrees

turtle.done()
