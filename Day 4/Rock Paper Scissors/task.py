import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# INSTRUCTOR CODE (ANOTHER WAY OF BUILDING THE CODE USING MATHS
game_images = [rock, paper, scissors]
choices = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
if choices >= 0 and choices <=2:
    print(game_images[choices])

computer = random.randint(0,2)
print("Computer chose: ")
print(game_images[computer])

if choices < 0 or choices > 2 :
    print("Invalid choice. Choose from 0 to 2")
elif choices == computer :
    print("Tie game!")
elif choices > computer :
    print("You win!")
elif choices < computer :
    print("You lose!")
elif choices == 0 and computer == 2 :
    print("You win!")
elif choices == 2 and computer == 0 :
    print("You lose!")
else :
    ()





# THIS IS MY CODE AND IT WORKS
# choices = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n")
# if choices == "0":
#     print(rock)
# elif choices == "1":
#     print(paper)
# elif choices == "2" :
#     print(scissors)
# else :
#     print("invalid input")
#
# computer = random.choice([rock, paper, scissors])
# # rock_paper_scissors = random.choice([computer])
# print(f"Computer chose: {computer}")
# if choices == "0":
#     if computer == rock:
#         print("Tie game!")
#     elif computer == scissors:
#         print("You win!")
#     else :
#         print("You lose!")
# if choices == "1":
#     if computer == rock:
#         print("You win!")
#     elif computer == paper:
#         print("Tie game!")
#     else :
#         print("You lose!")
# if choices == "2":
#     if computer == rock:
#         print("You lose!")
#     elif computer == paper:
#         print("You win!")
#     else :
#         print("Tie game!")
# else :
#     ()


