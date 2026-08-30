student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# total_scores = sum(student_scores)
# sum = 0
# for score in student_scores: #so u put variable first then the list
#     sum += score
# print(sum)
# print(range(1, 10))

max_score = 0
total_scores = sum(student_scores)
for score in student_scores:
    if score > max_score: #max score set at 0 due to first line, then it will compare the next score in the list
                          #which will be 150 then 150 is bigger than 0 then it will be set as the new max score
                          #next is 142 which is smaller than 150 then it will ignore and go on the list and so
        max_score = score
print(max_score)