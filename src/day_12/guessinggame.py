from .art import logo
import random

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5

def guess_number():
    print(logo)

    greeting_msg = """
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Choose a difficulty. Type 'easy' or 'hard': 
    """
    difficulty = input(greeting_msg).strip().lower()

    attempts = get_guesses_by_difficulty(difficulty)

    num_to_guess = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if int(guess) < num_to_guess:
            print("Too low.")
        elif int(guess) > num_to_guess:
            print("Too High.")
        else:
            print(f"You got it! The answer was {num_to_guess}.")
            break
        print("Guess again.")
        attempts-=1

    print("You've run out of guesses. Refresh the page to run again.")

def get_guesses_by_difficulty(difficulty):
    return EASY_LEVEL_GUESSES if difficulty == "easy" else HARD_LEVEL_GUESSES