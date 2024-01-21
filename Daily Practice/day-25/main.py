# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# avg = sum(temp_list)/len(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# print(data[data.day == "Monday"])

# max_temp_celsius = data[data.day == "Monday"]["temp"]
# max_temp_f = 9/5 * max_temp_celsius + 32
# print(max_temp_f)

# Create a dict from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
