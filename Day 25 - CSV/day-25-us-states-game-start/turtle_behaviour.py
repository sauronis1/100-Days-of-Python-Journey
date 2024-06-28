from turtle import Turtle
import pandas

states_data = pandas.read_csv("50_states.csv")

state_names_list = states_data["state"].to_list()
state_x_coor = states_data["x"].to_list()
state_y_coor = states_data["y"].to_list()
print(state_names_list)

states_dictionary = {
}

for i in range(len(state_names_list)-1):
    states_dictionary.update({state_names_list[i]: [state_x_coor[i], state_y_coor[i]]})


class Write_State_Name(Turtle):

    def __init__(self, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(states_dictionary[state_name][0], states_dictionary[state_name][1])
        self.write(arg=state_name, move=True, align="center", font=("Arial", 8, "normal"))
