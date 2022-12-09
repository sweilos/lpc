from turtle import *

shape("classic")
speed('fastest')


def draw_fractal(size, level, angle):
    if level == 0:
        color("green")
        dot(size)
        color("brown")
        return

    forward(size)
    right(angle)

    draw_fractal(size * 0.8, level - 1, angle)
    left(angle * 2)
    draw_fractal(size * 0.8, level - 1, angle)
    right(angle)
    backward(size)


left(90)
color("brown")
draw_fractal(50, 6, 25)


mainloop()
