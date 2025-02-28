from src.day_10.art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    should_continue = True
    new_number = True
    result = 0.0
    while should_continue:
        if new_number:
            print("\n" * 20)
            print(logo)
            first_number = float(input("What's the first number?: "))
        else:
            first_number = result
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        result = operations[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result}")
        new_number = input(f"Type 'y' to continue calculating with {result},"
                           f" or type 'n' to start a new calculation: ").lower() == "n"
