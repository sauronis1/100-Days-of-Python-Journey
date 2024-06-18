from turtle import Turtle
from random import choice, randint
from level_manager import Level

POSSIBLE_COLORS = ["orange", "yellow", "blue", "red", "brown", "green", "pink"]
class Car(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.color(choice(POSSIBLE_COLORS))
        self.setheading(180)
        self.shapesize(None, 2)
        self.penup()
        self.speed = 3

    def move(self, speed):
        self.forward(self.speed+(speed+1))

    def teleport_to_right(self):
        random_y = randint(-240, 240)
        self.goto(310, random_y)