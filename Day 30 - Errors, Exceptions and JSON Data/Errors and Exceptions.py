# FilenotFound
# with open('a_file.txt') as file:
#    file.read()  # file not found error

# KeyError
# a_dict = {'key':'value'}
# value = a_dict["nonexistent_key"]

# Index Error
# fruit_list = ['apple', 'banana']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5) # str and int cannot mix

# Handling Exceptions
# try - execute something that might cause an exception
# except - do this if there was an exception
# else - do this if there were no exceptions
# finally - do this no matter what happens



# FilenotFound
# try:
#     file = open('a_file.txt') # if no file, print error msg
# except:
#     # print('there was an error')
#     file = open('a_file.txt', 'w')
#     file.write('something')

# However, if there is another code,
# try:
#     file = open('a_file.txt') # if no file, print error msg
#     a_dict = {'key':'value'}
#     value = a_dict["nonexistent_key"]
# except:
#     # print('there was an error')
#     file = open('a_file.txt', 'w') # this line will proceed irregardless of the dictionary value not found
#     file.write('something')

# To avoid this, we must indicate FileNotFoundError
try:
    file = open('a_file.txt') # if no file, print error msg
    a_dict = {'key':'value'}
    value = a_dict["key"]
except FileNotFoundError:
    # print('there was an error')
    file = open('a_file.txt', 'w') # this line will proceed regardless of the dictionary value not found
    file.write('something')
except KeyError as error_message:
    print(f'that key {error_message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file closed')
    # raise KeyError
    # raise TypeError('this is a TypeError')
# How to raise my own exceptions

height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError('height should not be over 3 metres.')

bmi = weight / height**2
print(bmi)
