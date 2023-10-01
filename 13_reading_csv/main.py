# import csv
#
# with open("weather_data.csv") as file:
#     obj = csv.reader(file)
#     for row in obj:
#         print(row)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data["temp"])
data_to_dict = data.to_dict()
print(data_to_dict)
print(data_to_dict["day"])
