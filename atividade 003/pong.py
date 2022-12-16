import turtle
import vlc

# draw screen
screen = turtle.Screen()
screen.title("Pong refactored by Yago")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw left paddle
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350, 0)

# draw right paddle
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_l_up():
    y = paddle_l.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_l.sety(y)


def paddle_l_down():
    y = paddle_l.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_r.sety(y)


# keyboard
screen.listen()
screen.onkeypress(paddle_l_up, "w")
screen.onkeypress(paddle_l_down, "s")
screen.onkeypress(paddle_r_up, "Up")
screen.onkeypress(paddle_r_down, "Down")

# game loop
while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball collision with upper wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        vlc.MediaPlayer('bounce.wav')

    # ball collision with lower wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        vlc.MediaPlayer('bounce.wav')

    # ball collision with right wall
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        vlc.MediaPlayer('bleep_sound.wav')

    # ball collision with left wall
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        vlc.MediaPlayer('bleep_sound.wav')
    # collision with right paddle
    if (340 < ball.xcor() < 350) and paddle_r.ycor() + 50 > ball.ycor() > paddle_r.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        vlc.MediaPlayer('bounce.wav')

    # collision with left paddle
    if (-340 > ball.xcor() > -350) and paddle_l.ycor() + 50 > ball.ycor() > paddle_l.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        vlc.MediaPlayer('bounce.wav')
