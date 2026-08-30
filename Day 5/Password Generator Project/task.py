letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
# import random
# password = ""
# #we can also use range(0, nr_letters) = range(1, nr_letters + 1)
# for letter in range(1 , nr_letters + 1): #whatever number user puts here means how many times the loop will run
#     password += random.choice(letters) #example if its 4, the empty password will run random 4 times
# for symbol in range(1 , nr_symbols + 1):
#     password += random.choice(symbols)
# for number in range(1 , nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

#Hard Level
import random
password_list = [] #[] = list instead of "" which is a string
#we can also use range(0, nr_letters) = range(1, nr_letters + 1)
for letter in range(1 , nr_letters + 1):
    password_list.append(random.choice(letters)) #append = add 1 value/letter to the add of the list
                                                 #basically for letter in range(1 , nr_letters + 1): means
                                                 #user will choose a number(eg.4) and this line will run 4 times
                                                 #grabbing 4 random letters from the letters list and append
                                                 #meaning add 4 random letters to the back of the list which is
                                                 #password_list = [] which is an empty list
for symbol in range(1 , nr_symbols + 1):
    password_list.append(random.choice(symbols))
for number in range(1 , nr_numbers + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list) #shuffle the password list after adding everything

password = ""
for char in password_list: #convert it back into a string instead of leaving it
                           #looking like this ['G', '5', '4', '&', 'r', '&', '6', '*', '3', '*', 'g', 'P']
    password += char
print(f"Your password is: {password}")