#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


with open("./Input/Letters/starting_letter.txt") as file:
    letters = file.read()

for name in names:
    clean_name = name.strip()
    new_letters = letters.replace("[name]", clean_name)
    print(new_letters)
    with open(f"./Output/ReadyToSend/Letter_for_{clean_name}.text", mode = "w") as file:
        file.write(new_letters)