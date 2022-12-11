from turtle import *

shape("classic")
speed('fastest')

def drawFractal (size, level, angle):

    if level == 0:
        color("green")
        dot(size)
        color("brown")
        return

    forward(size)
    right(angle)
    drawFractal(size * 0.8, level - 1, angle)
    left(angle * 2)
    drawFractal(size * 0.8, level - 1, angle)
    right(angle)
    backward(size)

left(90)
color("brown")
drawFractal(70, 5, 25)

mainloop()
