try :
    age = int(input("How old are you?"))

except ValueError:
    print("Please enter with a number")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else :
    print(f"You need to be minimum of age 19 to drive.")
