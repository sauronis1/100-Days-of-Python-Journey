import turtle
import pandas as pd
from turtle_behaviour import Write_State_Name

# Setting up the screen
screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)

turtle.shape(image)

# Let's get the States' names in a list
states_data = pd.read_csv("50_states.csv")
states_names_list = states_data["state"].to_list()

# The game itself
states_answered = []
while len(states_answered) < 50:
    answer_state = screen.textinput(title=f"{len(states_answered)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    # If user guesses correctly
    if answer_state in states_names_list:
        states_answered.append(answer_state)
        states_names_list.remove(answer_state) # To make sure AS doesn't just type "Texas" 50 times
        new_state_name = Write_State_Name(answer_state)

# Make a file with state names to be learned
missing_states = pd.DataFrame(states_names_list)
missing_states.to_csv("States_to_learn.csv")