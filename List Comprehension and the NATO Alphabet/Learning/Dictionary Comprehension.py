#new_dict = {new_key : new_value for item in list}
# and also
#new_dict = {new_key : new_value for (key, value) in dict.items() if test}
import random

import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1,100) for student in names}
print(students_scores)
passed_students = {student : score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


#how to iterate over dataframe
import pandas

student_dict = {"student" : ["Angela", "James", "Lily"],
                "scores" : [56, 76, 98]
                }
#looping through dictionaries
#for (key,value) in student_dict.items() :
#   print(value)
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.scores)

