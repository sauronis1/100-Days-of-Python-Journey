from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        ball_y = random.choice([-1, 1])
        ball_x = random.choice([-1, 1])
        self.x_direction = ball_x
        self.y_direction = ball_y

    def move(self):
        new_x = self.xcor() + (self.x_move*self.x_direction)
        new_y = self.ycor() + (self.y_move*self.y_direction)
        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        self.y_direction *= -1

    def bounce_off_paddle(self):
        self.x_move += 2
        self.y_move += 2
        self.x_direction *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_direction *= -1
        self.x_move = 10
        self.y_move = 10
