from src.day_1.band_name_generator import  generate_band_name


def execute_program(choice):
    match choice:
        case "day_1":
            generate_band_name()
        case _:
            print("Wrong option selected! Please select the correct option.")


def execute_main():
    execute_program(input("Which program do you want to execute? "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
