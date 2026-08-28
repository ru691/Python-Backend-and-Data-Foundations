# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(len(states_of_america)) = amount inside the list but it counts from 1 instead of 0
# this means my last item is actually numbered 49 but the len states 50 cause it starts counting from 0
# numb_of_states = len(states_of_america) #50
#
# print(states_of_america[numb_of_states - 1])

# dirty_dozens = ("Cherry", "Apple", "Pear", "Cucumber", "Kale", "Spinach")
# BUT what if i want to separate vegetables and fruits and make a list inside a list

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinach"]
dirty_dozens = [fruits, veg]
print(dirty_dozens)

# if we want a specific item from the list we can do :
# print(dirty_dozens[1][1]) = Kale. Why?
# dirty_dozens[1][1] = the first [1] means the list, fruits = list 0 and veg = list 1
# the second [1] means the position after the list has been chosen :
# [1][1] = choose veg list then point out Kale