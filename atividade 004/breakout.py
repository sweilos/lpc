import turtle

# screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)

# paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("cyan")
paddle.shapesize(stretch_wid=0.5, stretch_len=3)
paddle.penup()
paddle.goto(0, -300)


def paddle_right():
    x = paddle.xcor()
    if x < 300:
        x += 30
    else:
        x = 300
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    if x > -300:
        x += -30
    else:
        x = -300
    paddle.setx(x)

screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")


while True:
    screen.update()
