import turtle
import pandas as pd
from turtle_behaviour import Write_State_Name

#Setting up the screen
screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)

turtle.shape(image)

#Let's get the States' names in a list
states_data = pd.read_csv("50_states.csv")
states_names_list = states_data["state"].to_list()
print(states_names_list)

#The game itself
number_of_states_answered = 0
game_not_finished = True
while game_not_finished:
    answer_state = screen.textinput(title=f"{number_of_states_answered}/50 States Correct",
                                    prompt="What's another state's name?").title()

    #If user guesses correctly
    if answer_state in states_names_list:
        number_of_states_answered += 1
        states_names_list.remove(answer_state) #To make sure AS doesn't just type "Texas" 50 times
        new_state_name = Write_State_Name(answer_state)

    if number_of_states_answered == 50:
        game_not_finished = False

turtle.mainloop()