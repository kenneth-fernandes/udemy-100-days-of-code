from src.day_16.menu import MenuItem


class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self) -> None:
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")


    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """Returns True when order can be made, False if ingredients are insufficient."""
        for key, value in drink.ingredients.items():
            if value > self.resources[key]:
                print(f"Sorry there is not enough {key}.")
                return False
        return True


    def make_coffee(self, order: MenuItem) -> None:
        """Deducts the required ingredients from the resources."""
        for ingredient, quantity in order.ingredients.items():
            self.resources[ingredient] -= quantity
        print(f"Here is your {order.name} ☕️. Enjoy!")