from turtle import Turtle

class Player(Turtle):

    def __init__(self, player_color):
        super().__init__(shape="turtle")
        self.color(player_color)
        self.left(90)
        self.penup()
        self.goto(0, -280)

    def move(self):
            self.forward(15)

    def create_car(self):
        self.__init__()