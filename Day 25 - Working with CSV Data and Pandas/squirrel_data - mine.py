import pandas
import pandas as pd

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# printing out the column names
# for col in data.columns:
#     print(col)

unique_colors = data['Primary Fur Color'].unique()
fur_colors = []
for color in unique_colors:
    fur_colors.append(color)
print(fur_colors)

# print(data.info())
fur_color_data = data['Primary Fur Color'].value_counts()
data2 = pandas.DataFrame(fur_color_data)
print(data2)