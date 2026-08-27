# % = divide two values and the remaining left over will be the value
# eg. 6 % 2 = 0 cause 6/2 = 3, clean division no decimal
# eg. 6 % 5 = 1 cause 6/5 = 1.2, think about a donut box that has 6 pieces and shared with 5 people
# 6 pieces total - 5 people who take 1 each = 1 donut left over so 6 % 5 = 1
# eg. 6 % 4 = 2 cause 6/4 = 1.5, same thing. a donut box with 6 pieces and 4 people sharing
# 6 pieces total - 4 people take 1 each = 2 donut left over so 6 % 4 = 2
#for 10 % 3 = 1, because 10 donuts and 3 people, each person take 3 donuts = 9 and there will be 1 left over
#Basically whatever the front value is, we will use the modula to divide it cleanly then the remainder will be the answer
#100 % 5 = 0, 100 % 6 = 6 x 16 = 96 with 4 remaining. 100 % 6 = 4

number = 100 % 6
print(number)

#Pause 2
number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("even")
else :
    print("odd")
