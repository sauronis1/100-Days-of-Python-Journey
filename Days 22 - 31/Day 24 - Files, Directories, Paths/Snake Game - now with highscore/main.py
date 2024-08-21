from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

"""setting up the screen"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game - now with highscore")
screen.tracer(0)

"""snake behaviour"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""the game itself"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    """detect collision with food"""
    if snake.head.distance(food) < 15:
        food.refresh()
        food_too_close_not_checked = True
        while food_too_close_not_checked:
            food_too_close = False
            for segment in snake.segments:
                if segment.distance(food) < 20:
                    food_too_close = True
            if food_too_close:
                food.refresh()
            else:
                food_too_close_not_checked = False
        snake.extend()
        scoreboard.increase_score()

    """detect collision with a wall"""
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    """detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
