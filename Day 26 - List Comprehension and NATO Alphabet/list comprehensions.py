# for loop

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# list comprehension

# new_list2 = [new_item for item in list]

# new_list2 = [n+1 for n in numbers]
# print(new_list2)

name = 'ANGELA'
letter_list = [letter for letter in name]
print(letter_list)


# new_nums = [num * 2 for num in range(1,5)]
# print(new_nums)