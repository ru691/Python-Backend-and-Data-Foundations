import random


# import my_module = created myself and opened in a separate tab that i coded
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# print(my_module.my_favorite_number) = basically is the same as random.randint.
# my_module = random and my_favorite_number = randit


#random.random 0 to 1 = 0 <= n < 1
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# #random.uniform 0 to 1 = 0 <= n <= 1
# random_float = random.uniform(0, 1)
# print(random_float)

head_tails = random.randint(1, 2)
if head_tails == 1:
    print("Heads")
else :
    print("Tails")
