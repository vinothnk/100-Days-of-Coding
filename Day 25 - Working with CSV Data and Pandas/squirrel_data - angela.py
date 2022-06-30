import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels, red_squirrels, black_squirrels]
}

data2 = pandas.DataFrame(data_dict)
print(data2)
data2.to_csv('squirrel_count.csv')