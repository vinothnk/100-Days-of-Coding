# new_dict = {new_key:new_value for item in list) # creating a new dictionary based on a list

# new_dict = {new_key:new_value for (key,value) in dict.items()} # creating a new dictionary based on an existing dictionary

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# scores = [random.randint(0,100) for num in range(len(names))]
# print(scores)
#
# student_scores = {names:scores for names,scores in zip(names, scores)}
# print(student_scores)

# OR

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passed_students)