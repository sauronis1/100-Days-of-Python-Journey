from turtle import Turtle


class DashedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.width(5)
        self.color("white")
        self.goto(0, -280)
        self.left(90)
        self.create_dashed_line()

    def create_dashed_line(self):
        for _ in range(17):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(12)
        self.pendown()
        self.forward(20)