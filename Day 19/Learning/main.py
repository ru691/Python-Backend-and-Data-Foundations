        ## READ THE FILE
with open("../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

        ##REWRITE THE FILE
# with open("my_file.txt", mode = "w") as file:
#     file.write("New text")

        ##APPEND THE FILE, ADD NEW THINGS INSTEAD OF REWRITING WHOLE THING
# with open("my_file.txt", mode = "a") as file:
#     file.write("\nNew text")

        ##CREATE NEW FILE
# with open("my_file.txt", mode = "w") as file:
#     file.write("Hello World")
#