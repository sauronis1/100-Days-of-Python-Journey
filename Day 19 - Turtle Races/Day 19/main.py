from turtle import Turtle, Screen

arnie = Turtle()
screen = Screen()


### GO FORWARDS ###
w_held_down = None
def move_forwards():
    global w_held_down
    w_held_down = True


def stop_moving_forwards():
    global w_held_down
    w_held_down = False


### GO BACKWARDS ###
s_held_down = None
def move_backwards():
    global s_held_down
    s_held_down = True


def stop_moving_backwards():
    global s_held_down
    s_held_down = False

def clear_screen():
    screen.clearscreen()
    arnie.home()


def moving():
    if w_held_down:
        arnie.forward(5)
    elif s_held_down:
        arnie.back(5)

screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeyrelease(fun=stop_moving_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeyrelease(fun=stop_moving_backwards, key="s")

screen.ontimer(moving, 250)
screen.exitonclick()



