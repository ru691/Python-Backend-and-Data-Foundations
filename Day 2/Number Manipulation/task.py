bmi = 84 / 1.65 ** 2
print(bmi) #print everything with decimal
print(int(bmi)) #print number only, no decimal
print(round(bmi)) #print rounded whole number, either 0.5 up or down
print(round(bmi, 2))  #round it to 2 decimal

score = 0
#assignment : basically use previous number and add/minus/divide or multiply
#example : everything user scores 1, add 50 (same thing for minus/divide or multiply
score += 50
print(score)

#f-strings : help you convert everything in the bracket just by adding f in front. no need to manual convert
#remember to add {} for different types of variable/expression
score = 0
height = 1.8
is_winning = True
print(f"your score is: {score}")
print(f"your height is: {height}")
print(f"is_winning is: {is_winning}")

#OR we can add all into one line
print(f"your score is: {score}, your height is: {height}, is winning: {is_winning}")
