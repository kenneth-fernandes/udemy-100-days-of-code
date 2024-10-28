
def calculate_tip():
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much percentage of tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    tip_amount = (bill * (tip/100))

    total_bill = bill + tip_amount

    each_person_pay = total_bill/people

    print(f"Each person should pay: {round(each_person_pay, 2)}")
