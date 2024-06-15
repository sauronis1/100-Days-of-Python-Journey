from turtle import Turtle, Screen

arnie = Turtle()
screen = Screen()


def move_forwards():
    arnie.forward(10)


def move_backwards():
    arnie.back(10)


def counter_clockwise():
    arnie.left(10)


def clockwise():
    arnie.right(10)


def clear_screen():
    screen.resetscreen()
    arnie.home()


screen.listen()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
