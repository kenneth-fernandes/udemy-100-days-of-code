import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/']


def generate_password():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    passwd_gen_level = int(input("Which level of password would you like? Type 1 for easy and 2 for hard. \n"))

    generated_password = ""

    match passwd_gen_level:
        case 1:
            generated_password = generate_easy_password(nr_letters, nr_symbols, nr_numbers)
        case 2:
            generated_password = generate_hard_password(nr_letters, nr_symbols, nr_numbers)
        case _:
            print("Wrong option selected! Select 1 for easy and 2 for hard.")

    print(generated_password)


def generate_easy_password(nr_letters, nr_symbols, nr_numbers):
    generated_password = ""

    for i in range(0, nr_letters):
        generated_password += random.choice(letters)

    for i in range(0, nr_symbols):
        generated_password += random.choice(symbols)

    for i in range(0, nr_numbers):
        generated_password += random.choice(numbers)

    return generated_password


def generate_hard_password(nr_letters, nr_symbols, nr_numbers):
    generated_passwd_list = []

    for i in range(0, nr_letters):
        generated_passwd_list.append(random.choice(letters))

    for i in range(0, nr_symbols):
        generated_passwd_list.append(random.choice(symbols))

    for i in range(0, nr_numbers):
        generated_passwd_list.append(random.choice(numbers))

    random.shuffle(generated_passwd_list)

    generated_password = ""
    for ch in generated_passwd_list:
        generated_password += ch

    return generated_password


