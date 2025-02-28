from src.day_15.coffee_menu_resources import MENU, resources

on_status = True
profit = 0

def start_machine() -> None:
    global on_status

    while on_status:

        customer_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        match customer_choice:
            case "report":
                print_machine_report()
            case "off":
                on_status = False
            case "espresso" | "latte" | "cappuccino":
                process_coffee_request(customer_choice)
            case _:
                print("Wrong option selected! Please select the correct option.")

    print("Shutting down the machine!")


def process_coffee_request(coffee_type) -> None:
    global profit
    ingredients: {} = MENU[coffee_type]['ingredients']

    # Checking if resources are sufficient for preparing a coffee
    is_resources_sufficient_str: str = check_resources_sufficient(coffee_type, ingredients)
    if is_resources_sufficient_str != "sufficient":
        print(is_resources_sufficient_str)
        return

    customer_amount = collect_and_process_coins()

    # Checking if user has enough money to buy a coffee
    is_money_sufficient_str: str = check_money_sufficient(coffee_type, customer_amount)
    if is_money_sufficient_str != "sufficient":
        print(is_money_sufficient_str)
        return

    # calculate cost and remaining change
    remaining_amount = customer_amount - MENU[coffee_type]['cost']

    # Update the profit of the coffee machine
    profit += MENU[coffee_type]['cost']

    # prepare coffee
    for ingredient, quantity in ingredients.items():
        resources[ingredient] -= quantity

    # Return remaining change to the customer
    if remaining_amount > 0.0:
        print(f"Here is ${remaining_amount} in change.")

    print(f"Here is your {coffee_type} Enjoy!")


def print_machine_report() -> None:
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def collect_and_process_coins() -> float:
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters?: ")) * 0.25
    dimes_amount = int(input("How many dimes?: ")) * 0.10
    nickles_amount = int(input("How many nickles?: ")) * 0.05
    pennies_amount = int(input("How many pennies?: ")) * 0.01

    return quarters_amount + dimes_amount + nickles_amount + pennies_amount


def check_money_sufficient(coffee_type: str, customer_amount: float) -> str:
    return "Sorry that's not enough money. Money refunded." \
        if MENU[coffee_type]['cost'] > customer_amount \
        else "sufficient"


def check_resources_sufficient(coffee_type: str, ingredients: {}) -> str:
    for key, value in ingredients.items():
        if value > resources[key]:
            return f"Sorry there is not enough {key}."
    return "sufficient"