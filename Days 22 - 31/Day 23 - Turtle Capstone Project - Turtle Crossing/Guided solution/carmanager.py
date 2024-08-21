from turtle import Turtle
from random import choice, randint
from level_manager import Level

STARTING_MOVE_DISTANCE = 5
POSSIBLE_COLORS = ["orange", "yellow", "blue", "red", "brown", "green", "pink"]
SPEED = 1

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = SPEED

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(1, 2)
            new_car.color(choice(POSSIBLE_COLORS))
            new_car.penup()
            random_y = randint(-240, 240)
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE*self.speed)
