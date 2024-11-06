from src.day_1.band_name_generator import generate_band_name
from src.day_2.tip_calculator import calculate_tip
from src.day_3.treasure_island import find_the_treasure
from src.day_4.rock_paper_scissors import play_rock_paper_scissors
from src.day_5.password_generator import generate_password
from src.day_7.hangman_game import play_game


def execute_program(choice):
    match choice:
        case "day_1":
            generate_band_name()
        case "day_2":
            calculate_tip()
        case "day_3":
            find_the_treasure()
        case "day_4":
            play_rock_paper_scissors()
        case "day_5":
            generate_password()
        case "day_7":
            play_game()
        case _:
            print("Wrong option selected! Please select the correct option.")


def execute_main():
    execute_program(input("Which program do you want to execute? "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
