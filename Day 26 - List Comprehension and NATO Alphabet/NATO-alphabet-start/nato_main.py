import pandas as pd
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv('nato_phonetic_alphabet.csv')

# for (key, value) in df.items():
#     print(key, value)

# for (index, row) in df.iterrows():
#     print(row.letter, row.code)

alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(alpha_dict)
# print(alpha_dict['A'])
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input('Please enter a word: ').upper()
word_list = [alpha_dict[letter] for letter in word]
print(word_list)