import turtle
import random
import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)


rgb_colors = []
colors = colorgram.extract('signal.jpeg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

arnie = Turtle()
arnie.teleport(-200,-100)
arnie.hideturtle()
def draw_a_line_of_dots():
    arnie.up()
    for _ in range(10):
        arnie.dot(20, random.choice(rgb_colors))
        arnie.forward(40)


def draw_a_hirst():
    y = -100
    for _ in range(10):
        draw_a_line_of_dots()
        y += 40
        arnie.teleport(-200, y)

draw_a_hirst()



screen = Screen()
screen.exitonclick()
