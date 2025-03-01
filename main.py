from src.day_01.band_name_generator import generate_band_name
from src.day_02.tip_calculator import calculate_tip
from src.day_03.treasure_island import find_the_treasure
from src.day_04.rock_paper_scissors import play_rock_paper_scissors
from src.day_05.password_generator import generate_password
from src.day_07.hangman_game import play_game as play_hangman_game
from src.day_08.ceasar_cipher import ceaser_cipher
from src.day_09.secret_auction import start_secret_auction
from src.day_10.calculator import calculator
from src.day_11.blackjack import play_game as play_blackjack_game
from src.day_12.guessinggame import guess_number
from src.day_14.v1.higher_lower_game import play_game as play_higher_lower_game_v1
from src.day_14.v2.higher_lower_game import play_game as play_higher_lower_game_v2
from src.day_15.coffee_machine import start_machine as start_coffee_machine
from src.day_16.coffee_machine_driver import CoffeeMachineDriver
from src.day_17.quiz_project import QuizProject


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
            play_hangman_game()
        case "day_08":
            ceaser_cipher()
        case "day_09":
            start_secret_auction()
        case "day_10":
            calculator()
        case "day_11":
            play_blackjack_game()
        case "day_12":
            guess_number()
        case "day_14_v1":
            play_higher_lower_game_v1()
        case "day_14_v2":
            play_higher_lower_game_v2()
        case "day_15":
            start_coffee_machine()
        case "day_16":
            CoffeeMachineDriver.get_instance().start_coffee_machine()
        case "day_17":
            QuizProject.play_game()
        case _:
            print("Wrong option selected! Please re-run and select the correct option.")


def execute_main():
    execute_program(input("Which program do you want to execute? "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
