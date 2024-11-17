import random
from src.day_07.hangman_words import word_list
from src.day_07.hangman_pics import hangman_pics


def play_game():
    # Choose a random word from the word_list
    chosen_word = random.choice(word_list)
    place_holder = ""

    for i in range(0, len(chosen_word)):
        place_holder += "_"

    tries = 0
    collected_letters = []

    game_over = False

    while tries < 6 and not game_over:
        print(place_holder)

        # Ask user to guess a letter
        guessed_letter = input("Guess a letter: ").lower()
        print(f"Guess letter: {guessed_letter}")

        place_holder = ""
        guess_wrong = True

        # Check if the letter guessed is one of the letter from the chosen_word
        for letter in chosen_word:
            if letter == guessed_letter:
                place_holder += letter
                collected_letters.append(guessed_letter)
                guess_wrong = False
            elif letter in collected_letters:
                place_holder += letter
            else:
                place_holder += "_"

        if guess_wrong:
            tries += 1

        print(hangman_pics[tries])

        if "_" not in place_holder:
            game_over = True
            print("You guessed the word correctly. You Win!!!")

    if tries >= 6:
        print(f"You Lose!!! The correct word was \"{chosen_word}.")