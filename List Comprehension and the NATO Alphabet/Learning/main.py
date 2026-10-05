numbers = [1, 2, 3]
# new_list = []
# for n in numbers :
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

#new list = [the new item you want |for| the item |in| side the list]
new_list = [n + 1 for n in numbers] #same as above but we cut 4 lines into 1
print(new_list)

name = "Angela"
new_name = [letter for letter in name] #split the name into individual letters
print(new_name)

number_range = range(1, 5) # = 1,2,3,4
new_number_range = [n * 2 for n in number_range] # = 2,4,6,8
#   OR
new_range = [n * 2 for n in range(1, 5)] # = 2,4,6,8
print(new_range)

# Conditional List comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
four_letter_names = [name for name in names if len(name) <= 4]
print(four_letter_names)
capital_names = [name.upper() for name in names if len(name) > 4]
print(capital_names)