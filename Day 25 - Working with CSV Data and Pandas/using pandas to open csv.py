import pandas

data = pandas.read_csv('weather_data.csv')
print(data)

print(data['temp'])

data_dict = data.to_dict() # converting the rows and columns into a dictionary
print(data_dict)

temp_list = data['temp'].to_list() # converting the values of temp into a list
print(temp_list)

# calculate average temperature
total_temp = 0
for num in temp_list:
    total_temp += num
print(total_temp)
average_temp = round(total_temp / len(temp_list), 2)
print(average_temp)

print('-------------------------')

aver_temp = round(sum(temp_list) / len(temp_list), 1)
print(aver_temp)

print('-------------------------')

# finding the average temp using the mean method from pandas.series
print(round(data['temp'].mean(),1))

print('-------------------------')

# finding the max temp value using the max method from pandas.series
print(data['temp'].max())

print('-------------------------')

# get data from columns - can use either one. case-sensitive
# print(data['condition'])
print(data.condition)

print('-------------------------')

# get data from rows
print(data[data['day'] == 'Monday'])

print('-------------------------')

# pull out the row which has the highest temperature of the week
# print(data['temp'].max())
print(data[data['temp'] == data['temp'].max()])

# OR

print(data[data.temp == data.temp.max()])

print('-------------------------')

monday = data[data.day == 'Monday']
print(monday)

print('-------------------------')

# convert monday temp from celsius to farenheit
# celsius_temp = monday.temp
# print(celsius_temp)
farenheit_formula = (monday.temp * 1.8) + 32
print(farenheit_formula)

print('-------------------------')

# creating a dataframe from scratch

data_dict2 = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data2 = pandas.DataFrame(data_dict2)
print(data2)
data2.to_csv('new_data.csv')