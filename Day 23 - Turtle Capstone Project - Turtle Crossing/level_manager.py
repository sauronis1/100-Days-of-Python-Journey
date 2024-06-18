from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level_num = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.update_header()

    def update_header(self):
        self.clear()
        self.write(f"Level: {self.level_num}", False, "center", ("Courier", 15, "normal"))