import random
import art
print(art.logo)

answer = random.randint(1,100)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else :
        print("Invalid input.")
        return set_difficulty()


attempts = set_difficulty()

def guess_the_number(remaining_attempts):
    game_over = False
    user_guess = int(input("Make a guess: "))
    while remaining_attempts != 0 and game_over == False :
        if user_guess > answer:
            print("Your guess is too high.")
            remaining_attempts -= 1
        elif user_guess < answer:
            print("Your guess is too low.")
            remaining_attempts -= 1
        else :
            print(f"You got it right! The answer was {answer}.")
            game_over = True
        if remaining_attempts > 0 and game_over == False:
            print("Guess again.")
            print(f"You have {remaining_attempts} attempts to guess the number.")
            user_guess = int(input("Make a guess: "))
        elif remaining_attempts == 0:
            print("You ran out of attempts to guess the number.")
            print(f"The answer was {answer}.")
            game_over = True

guess_the_number(attempts)