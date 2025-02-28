from src.day_09.art import gavel


bids = {}


def start_secret_auction():
    print(gavel)
    should_continue = True
    while should_continue:
        print("Welcome to the secret auction program.")
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))

        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "yes"
        if should_continue:
            print("\n" * 20)
        else:
            highest_bidder = ""
            bid_amount = 0
            for person in bids:
                if bids[person] > bid_amount:
                    highest_bidder = person
                    bid_amount = bids[person]
            print("\n" * 20)
            print(f"The winner is {highest_bidder} with a bid of ${bid_amount}.")