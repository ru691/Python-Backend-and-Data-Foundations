print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
directions = input('You have stumbled across a cross section. Choose to turn "left" or "right"?\n').lower()
if directions == "left" :
    actions = input('You have come across the black lake. Will you "swim" or "fly?"\n').lower()

    if actions == "fly" :
        door = input('You have arrived at the end point. There are three doors "Yellow", "Blue", "Red".'
              ' Which one will you choose\n').lower()
        if door == "yellow" :
            print("You have the treasure room. You won!")
        elif door == "blue" :
            print("You got struck by lightning and died. Game over.")
        elif door == "red" :
            print("You met the devil and got burned to death. Game over.")
        else :
            print("You chose a door that doesn't exist. You died, game over.")
    else :
        print("You got attacked by a drown and died. Game over.")

else :
    print("You got crushed by a boulder and died. Game over.")

