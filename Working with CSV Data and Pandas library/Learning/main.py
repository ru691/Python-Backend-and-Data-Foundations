# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
import pandas as pd

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["day"])
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# average_temp = pd.Series(temp_list).mean()
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())


# #Get data in columns
# print(data["temp"])
# print(data.temp)
# print(data["day"])

# #Get data in rows
# print(data[data.day == "Monday"]) #print monday row
# print(data[data.temp == data.temp.max()]) #print the highest temperature row
# monday = data[data.day == "Monday"] #get condition of monday/ get condition of the selected row
# print(monday.condition)
# monday_temp = (monday.temp * 9/5) + 32 #to get Fahrenheit
# print(monday_temp)

#create DataFrame from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
    }
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("students_score.csv") #turn dictionary into csv file