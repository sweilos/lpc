from turtle import *

Screen()


def triangle(x, y):

    penup()
    goto(x, y)
    pendown()

    for i in range(3):

        forward(100)
        left(120)
        forward(100)

onscreenclick(triangle, 1)
listen()
done()
