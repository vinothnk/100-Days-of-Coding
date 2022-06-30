# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]

with open('file1.txt') as file1:
    data1 = file1.readlines()
    stripped_data1 = [data.strip() for data in data1]
    print(stripped_data1)
#
with open('file2.txt') as file2:
    data2 = file2.readlines()
    stripped_data2 = [data.strip() for data in data2]
    print(stripped_data2)
#
common_nums = [i for i in stripped_data1 if i in stripped_data2]
print(common_nums)