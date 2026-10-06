#File not found error
# with open("a_file.txt") as a_file:
#     a_file.read()
# try : #try something that might not work, and if it does not we will execute the except block
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["key"]) #this will cause Key Error
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Hello")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else : #will only trigger if the try block succeeds
#     content = file.read()
#     print(content)
# finally : #will run no matter what
#     raise KeyError("I made this up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Unrealistic height")
bmi = weight / height ** 2
print(bmi)

#Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["a_key"]

#Index Error
# fruit_list = ["apple", "banana", "cherry"]
# fruit = fruit_list[4]

#Type Error
# text = "abc"
# print(text + 5)