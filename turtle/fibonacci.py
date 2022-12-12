from turtle import *
import math


def draw_lines():
    fibonacci = 1
    last_number = 0

    pencolor("blue")

    for i in range(4):
        forward(fibonacci * scale)
        left(90)
    right(90)

    temp = fibonacci
    fibonacci += last_number
    last_number = temp

    for i in range(1, n):
        backward(last_number * scale)
        right(90)

        for j in range(3):
            forward(fibonacci * scale)
            left(90)
        right(90)

        temp = fibonacci
        fibonacci += last_number
        last_number = temp

    penup()
    setposition(scale, 0)
    seth(90)
    pendown()


def draw_spiral():
    fibonacci = 1
    last_number = 0

    for i in range(n):

        print(fibonacci)

        move = math.pi * fibonacci * scale / 2
        move /= 90
        for j in range(90):
            forward(move)
            left(1)

        temp = fibonacci
        fibonacci += last_number
        last_number = temp


bgcolor("grey")
speed("fastest")

scale = 12

n = 8

draw_lines()
draw_spiral()

done()
