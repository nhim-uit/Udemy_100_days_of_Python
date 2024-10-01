# Udemy: Master Python by building 100 projects in 100 days
# Oct 1st, 2024
# Day 26 - List and Dictionary Comprehensions

import pandas, random

# list comprehension
ls = [1, 2, 3, 4, 5]
# print(ls)

new_ls = [i*i for i in ls]
# print(new_ls)

# dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

scores = {name: random.randint(1, 100) for name in names}
passed_students = {student: score for (student, score) in scores.items() if score >= 60}
print(scores)
print(passed_students)

# loop through data frame
student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98],
}

student_df = pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    if row.student == 'Angela':
        print(row)
