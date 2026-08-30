# for number in range(1, 11, 3): #range (1 , 10) means 1 to 9 not including 10, if we want 10 to be included
#                                #we wil need to use range (1,10)
#                                #the third number after the comma = addition of how much every run
#                                #range(1, 11, 3) = 1, 4(1+3), 7(4+3), 10(7+3)
#     print(number)

sum = 0
for number in range(1, 101):
    sum += number
print(sum)