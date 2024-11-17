import random


def play_rock_paper_scissors():
    while True:
        # Rock
        rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """

        # Paper
        paper = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """

        # Scissors
        scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

        moves = [rock, paper, scissors]

        users_move = moves[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))]

        computers_move = moves[random.randint(0, len(moves) - 1)]

        print(users_move)

        print("Computer chose: ")
        print(computers_move)

        if users_move == computers_move:
            print("Its a tie!")
        elif ((users_move == rock and computers_move == scissors) or
              (users_move == paper and computers_move == rock) or
              (users_move == scissors and computers_move == paper)):
            print("You win!")
        else:
            print("Computer wins!!")
