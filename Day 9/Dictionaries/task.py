programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again.",
}

# print(programming_dictionary["Bug"])
programming_dictionary["If"] = "If user does this, proceed. Else = do nothing." #basically add into dictionary
# print(programming_dictionary["If"])
# print(programming_dictionary)
programming_dictionary["Function"] = "Do it" #edit/change existing value inside dictionary
# print(programming_dictionary)

# programming_dictionary = {} #to wipe out existing dictionary before this line
# print(programming_dictionary)

#Loop through dictionary
for key in programming_dictionary:
    print(key) #print key (variable name)
    print(programming_dictionary[key]) #print value (variable meaning)