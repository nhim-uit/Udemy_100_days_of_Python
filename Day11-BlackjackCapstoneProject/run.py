from functions import *
from deck import deck


def run():
    chosen_cards = random.sample(deck, 4)
    update_deck(chosen_cards)

    # distribute cards to player and computer
    player_cards = chosen_cards[0:3:2]
    computer_cards = chosen_cards[1:4:2]
    board = create(player_cards, computer_cards)

    print(board)
    print(f"Your cards: {player_cards}, current points: {board['player']['points']}.")
    print(f"Computer's first card: {computer_cards[0]}.")

    # driver
    drive(board)

    # print result of the board
    print_res(board)
