from turtle import Turtle, Screen
from player_turtle import Player
from cars import Car
from level_manager import Level
from countdown import Countdown
import time
import random

def update_position_of_cars():
    for car in cars:
        random_x = random.randint(310, 7000)
        random_y = random.randint(-240, 240)
        car.goto(random_x, random_y)

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

#screen.textinput("Turtle color", "What colour would you like your turtle to be?").lower()
desired_color = "green"
player = Player(desired_color)

cars = []
for _ in range(500):
    new_car = Car()
    cars.append(new_car)
update_position_of_cars()

level = Level()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    for car in cars:
        car.move(level.level_num)
        if car.ycor() > player.ycor():
            if car.distance(player) < 25:
                game_is_on = False
        elif car.ycor() < player.ycor():
            if car.distance(player) < 18:
                game_is_on = False
        elif car.ycor() == player.ycor():
            if car.distance(player) < 20:
                game_is_on = False

    if player.ycor() > 280:
        level.level_num += 1
        level.update_header()
        update_position_of_cars()
        player.goto(0, -280)

    screen.update()
    countdown = Countdown()

screen.exitonclick()
