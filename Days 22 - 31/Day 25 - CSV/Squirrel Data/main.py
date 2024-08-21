"""
with open("weather_data.csv") as w_data:
    data = w_data.readlines()

print(data)
"""
"""
temperatures = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
print(temperatures)
"""

"""
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data.condition)
print(data["condition"])
"""
"""
#Get Data in Rows

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

monday_temp = monday.temp[0]
print(monday_temp * 9/5 + 32)
"""

#BB VERZE
import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

color_data = squirrel_data["Primary Fur Color"]
color_count_dic = {
    "Fur Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [],
}

color_count_dic["Count"].append(color_data.value_counts()["Gray"])
color_count_dic["Count"].append(color_data.value_counts()["Cinnamon"])
color_count_dic["Count"].append(color_data.value_counts()["Black"])

print(color_count_dic)

dataframe = pd.DataFrame(color_count_dic)
dataframe.to_csv("squirrel_fur_color_counts.csv")
print(dataframe)

#ANGELA VERZE
data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_fur.csv")
