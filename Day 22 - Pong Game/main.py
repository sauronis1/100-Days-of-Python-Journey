from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from dashes import DashedLine
import time

"""setting up the screen and the player paddles"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

"""scoreboard"""
scoreboard = Scoreboard()

"""dashed line in the middle"""
dash = DashedLine()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

"""right paddle controls"""
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

"""left paddle controls"""
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

"""the game itself"""
game_is_on = True
while game_is_on:
    time.sleep(0.08)
    scoreboard.update_scoreboard()
    screen.update()
    ball.move()

    """collision with an up or down wall"""
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_off_wall()

    """collision with a paddle"""
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_off_paddle()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_off_paddle()

    """collision with the right wall"""
    if ball.xcor() >= 390:
        ball.reset_position()
        scoreboard.l_point()

    """collision with the right wall"""
    if ball.xcor() <= -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
