import random
from .art import logo

def play_game():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    play_blackjack = get_play_blackjack()

    while play_blackjack:

        print(logo)
        play_another_card = True
        player_hands = [random.choice(cards)]
        dealer_hands = [random.choice(cards)]

        while play_another_card:
            player_hands.append(random.choice(cards))
            adjust_for_ace(player_hands)
            player_score = sum(player_hands)

            if player_score > 21:
                break
            print(f"    Your cards: {player_hands},  current score: {player_score}")
            print(f"    Computer's first card: {dealer_hands[0]}")
            play_another_card = get_play_another_card()

        players_final_score = sum(player_hands)
        dealers_score = sum(dealer_hands)

        if players_final_score <= 21:
            while dealers_score < 17:
                dealer_hands.append(random.choice(cards))
                adjust_for_ace(dealer_hands)
                dealers_score = sum(dealer_hands)

        outcome = determine_winner(player_hands, dealer_hands)
        print_outcome(player_hands, dealer_hands, outcome)

        play_blackjack = get_play_blackjack()
        print("\n" * 20)


def print_outcome(player_hands, dealer_hands, outcome):
    print(f"    Your final hand: {player_hands}, final score: {sum(player_hands)}")
    print(f"    Computer's final hand: {dealer_hands}, final score: {sum(dealer_hands)}")
    print(outcome)


def determine_winner(player_hands, dealer_hands):

    players_final_score = sum(player_hands)
    dealers_score = sum(dealer_hands)

    if players_final_score == dealers_score:
        return "It's a draw 🤝"
    elif dealers_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif players_final_score == 0:
        return "Win with a Blackjack 😎"
    elif players_final_score > 21:
        return "You went over. You lose 😭"
    elif dealers_score > 21:
        return "You win 😃"
    elif players_final_score > dealers_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def adjust_for_ace(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


def get_play_blackjack():
    greeting_msg = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    return input(greeting_msg).strip().lower() == "y"


def get_play_another_card():
    msg = "Type 'y' to get another card, type 'n' to pass: "
    return input(msg).strip().lower() == "y"