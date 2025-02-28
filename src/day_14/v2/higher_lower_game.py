import random

from src.day_14.v2.art import versus_logo, higher_lower_logo
from src.day_14.v2.followers import celebrities


def play_game() -> None:
    # print logo
    print(higher_lower_logo)

    # Retrieve celebs randomly for A
    celebrity_a: {} = retrieve_random_celeb(celebrities)

    # Initialize the score
    score = 0

    while True:
        # Retrieve celebs randomly for B
        celebrity_b: {} = retrieve_random_celeb(celebrities)

        # Continue retrieving celebs randomly for B if it matches A
        while celebrity_a['display_str'] == celebrity_b['display_str']:
            celebrity_b = retrieve_random_celeb(celebrities)

        # print input messages for A and B celebs
        print(f"Compare A: {celebrity_a['display_str']}. ({celebrity_a['followers']})")
        print(versus_logo)
        print(f"Against B: {celebrity_b['display_str']}. ({celebrity_b['followers']})")

        # Ask user input for their choice of which has more followers (A ro B)
        user_answer: str = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        # Check if the user input is correct
        user_result: {} = validate_user_answer(user_answer, celebrity_a, celebrity_b)

        if user_result['result']: # If user answered correctly, prompt again as well as mentioning the current score
            score += 1
            print(f"You're right! Current score: {score}")
            celebrity_a = user_result['higher_celeb_followers']
        else: # If user answered incorrectly, end the program with final score
            print("\n" * 20)
            print(higher_lower_logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

def retrieve_random_celeb(celebrity_list: []) -> {}:
    # Retrieve random celeb
    celebrity: {} = random.choice(celebrity_list)
    return build_celeb(celebrity)

def build_celeb(celebrity: {}) -> {}:
    celebrity_disp_str = (f"{celebrity['name']},"
                          f" {fetch_appropriate_article(celebrity['profession'])} {celebrity['profession']},"
                          f" from {celebrity['country']}")
    return {
        "display_str": celebrity_disp_str,
        "followers": celebrity['followers']
    }

def fetch_appropriate_article(word: str) -> str:
    return "an" if word.strip().lower()[0] in ['a', 'e', 'i', 'o', 'u'] else "a"

def validate_user_answer(user_answer: str, celebrity_a: {}, celebrity_b: {}) -> {}:

    higher_celeb_followers = celebrity_a \
        if celebrity_a['followers'] > celebrity_b['followers'] \
        else celebrity_b

    if user_answer == "A":
        user_celeb_answer: {} = celebrity_a
    elif user_answer == "B":
        user_celeb_answer: {} = celebrity_b
    else:
        return { "result": False, "higher_celeb_followers" : higher_celeb_followers }

    result: bool =  user_celeb_answer['display_str'].lower() == higher_celeb_followers['display_str'].lower()

    return { "result": result, "higher_celeb_followers" : higher_celeb_followers }



