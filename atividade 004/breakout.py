from random import randint
from time import sleep
from modules import collisions, sounds, utils, objects

ball_initial_position_x = 0
ball_initial_position_y = -220
playing = True
is_rolling = True
pause = False
shrink = False


def close_screen():
    global playing
    playing = not playing


screen = objects.create_screen("Breakout", 800, 600)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)
# drawing bricks
y = 200
for color in utils.colors.keys():
    objects.create_line_of_bricks(y, color)
    y -= 30

paddle = objects.create_paddle(0, -250, 0.8, 6, "blue")
ball = objects.create_ball(ball_initial_position_x,
                           ball_initial_position_y, "white")

# defining starting ball speed
if randint(0, 1) == 0:
    ball.dx = collisions.base_speed
else:
    ball.dx = -collisions.base_speed
ball.dy = 0


# left paddle
def paddle_left():
    global pause
    global shrink
    if not pause:
        x = paddle.xcor()
        if shrink is False:
            if x > -350:
                x += -30
            else:
                x = -350
            paddle.setx(x)
        else:
            if x > -355:
                x += -30
            else:
                x = -373
            paddle.setx(x)
        if is_rolling:
            ball.setx(ball.xcor() - 30)


# right paddle
def paddle_right():
    global pause
    global shrink
    if not pause:
        x = paddle.xcor()
        if shrink is False:
            if x < 340:
                x += 30
            else:
                x = 340
            paddle.setx(x)
        else:
            if x < 345:
                x += 30
            else:
                x = 367
            paddle.setx(x)
        if is_rolling:
            ball.setx(ball.xcor() + 30)


def throw_ball():
    global is_rolling
    if is_rolling:
        px = paddle.xcor()
        bx = ball.xcor()
        degrees = px - bx + 90
        collisions.calculate_angle(ball, degrees)
        is_rolling = False


def pause_game():
    global pause
    pause = not pause


# move paddle
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(throw_ball, "space")
screen.onkeypress(pause_game, "p")
score_hud = objects.create_hud(-250, 250)
life_hud = objects.create_hud(300, 250)
life_hud.color("red")


def update_hud():
    score_hud.clear()
    score_hud.write("SCORE {}".format(utils.score), align="center",
                    font=("Press Start 2P", 18, "normal"))
    life_hud.clear()
    # heart shape and size
    life_hud.write("\u2764" * utils.lifes, align="center",
                   font=("Press Start 2P", 24, "normal"))


update_hud()
while playing:
    # stop condition
    if utils.lifes == 0:
        update_hud()
        objects.end_game_screen("GAME OVER :(")
        sounds.play_defeat()
        sleep(2)
        playing = False
        continue
    if utils.inv_bricks == 28:
        update_hud()
        objects.end_game_screen("YOU WIN :)")
        sounds.play_victory()
        sleep(2)
        playing = False
        continue
    # ball movement
    if not pause:
        if is_rolling:
            ball.setx(ball.xcor() + ball.dx)
            paddle_half_width = paddle.shapesize()[1] * 10
            if ball.xcor() + 10 >= paddle.xcor() + paddle_half_width or \
                    ball.xcor() - 10 <= paddle.xcor() - paddle_half_width:
                ball.dx *= -1
        else:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
    if collisions.collision(paddle, ball):
        sounds.play_bounce()
        if shrink is False:
            objects.shrink_paddle(paddle, 0.8, 3)
            shrink = True
    for brick in objects.bricks:
        if collisions.collision_brick(brick, ball):
            sounds.play_bounce()
            brick.hideturtle()
            utils.inv_bricks += 1
            utils.update_score(brick.color()[0])
            update_hud()
    # right wall collision
    if ball.xcor() > 385:
        sounds.play_bounce()
        ball.setx(385)
        ball.dx *= -1
    # left wall collision
    if ball.xcor() < -388:
        sounds.play_bounce()
        ball.setx(-388)
        ball.dx *= -1
    # upper wall collision
    if ball.ycor() > 288:
        sounds.play_bounce()
        ball.dy *= -1
    # game restart
    if ball.ycor() < -300:
        utils.lifes -= 1
        update_hud()
        ball.goto(paddle.xcor(), ball_initial_position_y)
        ball.dx = collisions.base_speed
        ball.dy = 0
        is_rolling = True
        if randint(0, 1) == 0:
            ball.dx *= -1
    screen.update()
