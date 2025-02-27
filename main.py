from src.day_01.band_name_generator import generate_band_name
from src.day_02.tip_calculator import calculate_tip
from src.day_03.treasure_island import find_the_treasure
from src.day_04.rock_paper_scissors import play_rock_paper_scissors
from src.day_05.password_generator import generate_password
from src.day_07.hangman_game import play_game
from src.day_08.ceasar_cipher import ceaser_cipher
from src.day_09.secret_auction import start_secret_auction
from src.day_10.calculator import calculator
from src.day_11.blackjack import play_game

def execute_program(choice):
    match choice:
        case "day_01":
            generate_band_name()
        case "day_02":
            calculate_tip()
        case "day_03":
            find_the_treasure()
        case "day_04":
            play_rock_paper_scissors()
        case "day_05":
            generate_password()
        case "day_07":
            play_game()
        case "day_08":
            ceaser_cipher()
        case "day_09":
            start_secret_auction()
        case "day_10":
            calculator()
        case "day_11":
            play_game()
        case _:
            print("Wrong option selected! Please select the correct option.")


def execute_main():
    execute_program(input("Which program do you want to execute? "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
