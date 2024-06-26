from turtle import Turtle, Screen
from player_turtle import Player
from carmanager import CarManager
from level_manager import Level
import time
import random


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

desired_color = screen.textinput("Turtle color", "What colour would you like your turtle to be?").lower()
player = Player(desired_color)

car_manager = CarManager()

level = Level()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        level.level_num += 1
        level.update_header()
        player.goto(0, -280)
        car_manager.speed += 1

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    level.game_over(game_is_on)

    screen.update()

screen.exitonclick()
