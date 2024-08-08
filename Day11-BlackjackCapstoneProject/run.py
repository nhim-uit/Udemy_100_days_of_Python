from functions import *
from deck import deck


def run():
    """
    Driver of 1 Black Jack game
    :return: void
    """
    chosen_cards = random.sample(deck, 4)
    update_deck(chosen_cards)

    # Distribute cards to player and computer
    player_cards = chosen_cards[0:3:2]
    computer_cards = chosen_cards[1:4:2]
    board = create(player_cards, computer_cards)

    print(f"Your cards: {player_cards}, current points: {board['player']['points']}.")
    print(f"Computer's first card: {computer_cards[0]}.")
    print(board)

    # Driver
    drive(board)

    # Drint results of the board
    print_res(board)
