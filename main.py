# This is a sample Python script.

# with open("weather_data.csv") as file:
#     daily = file.readlines()
#
# print(daily)

# import csv
#
# with open("weather_data.csv") as file:
#     daily = csv.reader(file)
#     temperatures = []
#     line = 0
#     for row in daily:
#         if line > 0:
#             temperatures.append(int(row[1]))
#         line += 1
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # type(data)
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# avg = sum(temp_list) / len(temp_list)
#
# print(avg)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


