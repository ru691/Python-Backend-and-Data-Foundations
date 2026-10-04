import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261004.csv")
fur_color = data["Primary Fur Color"]
gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])

fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, cinnamon_fur, black_fur],
}
fur_data = pandas.DataFrame(fur_dict)
print(fur_data)
fur_data.to_csv("fur_data.csv")