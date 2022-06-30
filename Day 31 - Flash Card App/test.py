import random
import pandas as pd

df = pd.read_csv('C:/Users/wooo_/PycharmProjects/Day 31 - Flash Card App/data/french_words.csv')
# reading the csv 1st. then store into a dataframe.
df1 = df.to_dict(orient='records')

print(len(df1))

rand_no = random.randint(0,101)
print(df1[rand_no])
#convert the df to dictionary format
# print(df1)
#
# print(len(df1['French']))
# random_no = random.randint(0, 100)
# print(random_no)
#
#
# french_word = df1['French'][random_no]
# print(french_word)
#
# english_word = df1['English'][random_no]
# print(english_word)