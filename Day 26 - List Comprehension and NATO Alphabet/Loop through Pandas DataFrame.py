import pandas as pd

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 66, 76]
}
# looping through a dictionary
# for (key, value) in student_dict.items():
#     print(value)
# student_scores = {student:score for student, score in student_dict.items()}
# print(student_scores)

df = pd.DataFrame(student_dict)
print(df)

# looping through a dataframe

# for (key, value) in df.items():
#     print(key)
#     print(value)
# # not very useful

# use iterrows for looping through rows of a dataframe
for (index, row) in df.iterrows():
    # print(index)
    # print(row)
    print(row.student)
    print(row.score)