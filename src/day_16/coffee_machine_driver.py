from src.day_16.menu import Menu, MenuItem
from src.day_16.coffee_maker import CoffeeMaker
from src.day_16.money_machine import MoneyMachine



class CoffeeMachineDriver:
    _instance = None

    def __init__(self):
        self.menu: Menu = Menu()
        self.coffee_maker: CoffeeMaker = CoffeeMaker()
        self.money_machine: MoneyMachine = MoneyMachine()

    @staticmethod
    def get_instance():
        """Returns the singleton instance of the CoffeeMachineDriver class"""
        if CoffeeMachineDriver._instance is None:
            CoffeeMachineDriver._instance = CoffeeMachineDriver()
        return CoffeeMachineDriver._instance

    def start_coffee_machine(self):
        """Starts the coffee machine and prompts the customer for their order"""
        while True:
            customer_choice = input(f"What would you like? ({self.menu.get_items()[:-1]}): ").strip().lower()

            if customer_choice == "report":
                    self.coffee_maker.report()
                    self.money_machine.report()
            elif customer_choice ==  "off":
                    break
            else:
                self.__process_coffee_request(customer_choice)

        print("Shutting down the machine!")


    def __process_coffee_request(self, customer_choice: str) -> None:
        """Processes the customer's request and prepares the selected coffee"""

        drink: MenuItem | None = self.menu.find_drink(customer_choice)
        if drink is None:
            return

        if not self.coffee_maker.is_resource_sufficient(drink):
            return

        self.money_machine.process_coins()

        if not self.money_machine.make_payment(drink.cost):
            return

        self.coffee_maker.make_coffee(drink)