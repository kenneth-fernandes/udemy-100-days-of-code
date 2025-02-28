class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }


    def __init__(self):
        self.profit = 0
        self.money_received = 0


    def report(self) -> None:
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")


    def process_coins(self) -> None:
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin_type, coin_value in self.COIN_VALUES.items():
            self.money_received += int(input(f"How many {coin_type}?: ")) * coin_value


    def make_payment(self, cost: float) -> bool:
        """Returns True when payment is accepted, or False if insufficient."""
        if cost > self.money_received:
            self.money_received = 0
            print("Sorry that's not enough money. Money refunded.")
            return False

        # add cost to profit
        self.profit += cost

        # calculate remaining amount or change
        remaining_amount = round(self.money_received - cost, 2)

        if remaining_amount > 0.0:
            # print remaining change
            print(f"Here is your ${remaining_amount} in change.")
        self.money_received = 0

        return True