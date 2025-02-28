import random
from src.day_14.v1.art import higher_lower_logo, versus_logo
from src.day_14.v1.followers import celebrities


def play_game():
    print(higher_lower_logo)
    celebrities_categories = list(celebrities.keys())

    celeb_dict = get_celeb_category_with_details(celebrities_categories)
    person_a = build_celeb_dict(celeb_dict['category'], celeb_dict['details'])

    correct_ans = 0

    while True:
        celeb_dict = get_celeb_category_with_details(celebrities_categories)
        person_b = build_celeb_dict(celeb_dict['category'], celeb_dict['details'])

        while person_b["name_with_details"] == person_a["name_with_details"]:
            celeb_dict = get_celeb_category_with_details(celebrities_categories)
            person_b = build_celeb_dict(celeb_dict['category'], celeb_dict['details'])

        print(f"Compare A: {person_a['name_with_details']}.")
        print(versus_logo)
        print(f"Against B: {person_b['name_with_details']}.")

        correct_option = 'A' if person_a['followers'] > person_b['followers'] else 'B'
        correct_celeb = person_a if person_a['followers'] > person_b['followers'] else person_b

        user_answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if correct_option != user_answer:
            print("\n" * 20)
            print(higher_lower_logo)
            print(f"Sorry, that's wrong. Final score: {correct_ans}")
            break
        else:
            correct_ans+=1
            print(f"You're right! Current score: {correct_ans}")
            person_a = correct_celeb


def get_random_record(records):
    return random.choice(records)


def build_celeb_dict(celeb_category: str, celeb_details):
    celeb_category = celeb_category[:-1].capitalize()
    article = 'an' if celeb_category[0].lower() in ['a','e','i','o','u'] else 'a'
    return {
        'name_with_details': f"{celeb_details['name']}, {article} {celeb_category}, from {celeb_details['country']}",
        'followers': celeb_details['followers']
    }

def get_celeb_category_with_details(celebrities_categories):
    category = get_random_record(celebrities_categories)
    details = get_random_record(celebrities[category])

    return {
        "category": category,
        "details": details
    }