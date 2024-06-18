from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__("square")
        self.speed("fastest")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() >= 240:
            pass
        else:
            self.goto(self.xcor(), self.ycor()+25)

    def move_down(self):
        if self.ycor() <= -230:
            pass
        else:
            self.goto(self.xcor(), self.ycor()-25)
