def find_the_treasure():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
    ''')
    while True:
        print("Welcome to Treasure Island. "
              "Your mission is to find the treasure.")

        direction = input("You're at a crossroad, where do you want to go? "
                          "Type \"left\" or \"right\"? ").lower()

        if direction == "left":
            action = input("You arrive at the island unharmed. "
                           "There is a house with 3 doors. One red, "
                           "one yellow and one blue. "
                           "Which colour do you choose? ").lower()

            if action == "wait":
                door = input("Which door? (red, yellow or blue) ")

                if door == "yellow":
                    print("You found the treasure. You Win! \n")
                elif door == "red":
                    print("It's a room full of fire. Game Over. \n")
                elif door == "blue":
                    print("You enter a room of beasts. Game Over. \n")
                else:
                    print("You chose a door that doesn't exist. Game Over \n")

            else:
                print("You got attacked by an angry trout. Game Over. \n")

        else:
            print("ou fell into a hole. Game Over. \n")
