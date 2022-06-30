import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.min
print(year, month, day, hour, min)

day_of_week = now.weekday()
print(day_of_week)
# will start counting as 0
# Monday = 0
# Tues = 1
# Wed = 2
# Thur = 3
# Fri = 4
# Sat = 5
# Sun = 6

date_of_birth = dt.datetime(year=1984, month=8, day=9, hour=4, minute=30, second=30) # values are INT
print(date_of_birth)