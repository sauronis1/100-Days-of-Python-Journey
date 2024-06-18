from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def game_over(self):
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=("Courier", 70, "normal"))
        if self.r_score > self.l_score:
            self.goto(150, -20)
            self.write("Player 2 Wins!", align="center", font=("Courier", 20, "normal"))
        else:
            self.goto(-150, -20)
            self.write("Player 1 Wins!", align="center", font=("Courier", 20, "normal"))
