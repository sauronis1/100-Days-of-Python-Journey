from turtle import Turtle
from threading import Timer


class Countdown(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.print_countdown()

    def print_countdown_line(self, arg):
        self.write(arg, False, "center", ("Courier", 10, "normal"))

    def print_countdown_line_2(self):
        self.write("2...", False, "center", ("Courier", 10, "normal"))

    def print_countdown_line_1(self):
        self.write("1...", False, "center", ("Courier", 10, "normal"))

    def print_go(self):
        self.write("GO!", False, "center", ("Courier", 10, "normal"))

    def print_countdown(self):
        self.print_countdown_line("3...")
        t = Timer(1, self.print_countdown_line_2)
        t.start()
        t = Timer(1, self.print_countdown_line_1)
        t.start()
        t = Timer(1, self.print_go)
        t.start()