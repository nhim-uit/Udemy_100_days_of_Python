import random
from deck import deck
from CONSTANTS import *


def convert(face: str):
    """
    Convert string faces into integer value
    :param face: str
    :return: int
    """
    val = face[1:]
    if val == 'A':
        return A
    elif val == 'J' or val == 'Q' or val == 'K':
        return LETTER
    else:
        return int(val)


def calc_pts(faces: list):
    """
    Calculate sum all values of the faces
    :param faces: list
    :return: s: int
    """
    s = 0
    for i in faces:
        s += convert(i)

    return s


def create(player: list, computer: list):
    """
    :param player: list of faces created randomly (2 faces)
    :param computer: list of faces created randomly (2 faces)
    :return: dict, containing dict player and dict computer
    """
    return {
        'player':
            {
                'faces': player,
                'points': calc_pts(player),
            },
        'computer':
            {
                'faces': computer,
                'points': calc_pts(computer),
            }
    }


def update_board(board: dict, player: str):
    """
    Randomly choose a card from the deck
    Update 'board' dict with new calculated points
    :param board: a dict player's faces and points
    :param player: 'player' or 'computer'
    :return: void
    """
    # Choose 1 card
    chosen_card = random.sample(deck, 1)

    # Remove chosen card from the deck
    deck.remove(chosen_card[0])

    # Add the chosen card into the board
    board[player]['faces'].extend(chosen_card)

    # Calculate points
    new_pts = calc_pts(chosen_card)
    board[player]['points'] += new_pts

    # Check if there are aces in the list of cards of player
    # and update the board
    update_aces(board, player)


def update_aces(board: dict, player: str):
    """
    Change 'A' into '1' to calculate points
    if all points initially went over 21

    :param board: a dict player's faces and points
    :param player: 'player' or 'computer'
    :return: void
    """
    faces = board[player]['faces']
    aces = [i[1:] for i in faces]

    if 'A' in aces and board[player]['points'] > BJ:
        for i in range(len(faces) - 1):
            if aces[i] == 'A':
                board[player]['faces'][i] = board[player]['faces'][i].replace('A', '1')

        # recalculate after change all 'A' into '1'
        board[player]['points'] = calc_pts(faces)

        if faces[-1] == 'A' and board[player]['points'] > BJ:
            board[player]['faces'][-1] = board[player]['faces'][i].replace('A', '1')
            board[player]['points'] = calc_pts(faces)


def update_deck(cards: list):
    """
    Remove chosen cards from the deck

    :param cards: list of cards
    :return: void
    """
    for card in cards:
        deck.remove(card)


def check_win(board: dict):
    """
    Check and compare points between player and computer
    :param board: dict, player and computer info
    :return: str, states of winning
    """
    player_pts = board['player']['points']
    cmpt_pts = board['computer']['points']

    if cmpt_pts > BJ and player_pts > BJ:
        return 'draw'
    elif cmpt_pts > BJ:
        return 'win'
    elif player_pts > BJ:
        return 'lose'
    else:
        if cmpt_pts < player_pts:
            return 'win'
        elif cmpt_pts == player_pts:
            return 'draw'
        else:
            return 'lose'


def check_over(board: dict, player: str):
    """
    Check if points went over 21
    :param board: dict
    :param player: str
    :return: boolean
    """
    if board[player]['points'] > BJ:
        return True

    return False


def check_bj(board: dict, player: str):
    """
    Check if BlackJack (21)
    :param board: dict
    :param player: str
    :return: boolean
    """
    if board[player]['points'] == BJ:
        return True

    return False


def computer_continue(board: dict):
    """
    Computer continues to randomly pick cards
    until going over 21, winning over player's points or still under 16
    :param board: dict
    :return: void
    """
    while board['computer']['points'] <= BJ \
            and board['computer']['points'] < board['player']['points'] \
            or board['computer']['points'] < AGE:
        update_board(board, 'computer')
        print(board)


def print_res(board: dict):
    """
    Print the results
    :param board: dict
    :return: void
    """
    # Compare to get the resulted string
    res = check_win(board)

    # Print the results
    if res == 'win':
        print(f"Player wins with {board['player']['points']} points.")
    elif res == 'lose':
        print(f"Computer wins with {board['computer']['points']} points.")
    elif res == 'draw':
        print(f"Player and computer draw with: "
              f"player ({board['player']['points']} pts), " 
              f"computer ({board['computer']['points']} pts).")

    print(f"Computer's faces: {board['computer']['faces']}. ")


def drive(board: dict):
    """
    While loop of 1 BlackJack game
    :param board: dict
    :return: void
    """
    done = False

    while not done:
        update_aces(board, 'player')
        update_aces(board, 'computer')

        # Check if player's points or computer's points equal 21
        if check_bj(board, 'player') or check_bj(board, 'computer'):
            return

        # Check if player went over 21
        if check_over(board, 'player'):
            # If player's points went over 21,
            # computer continue to pick cards if initial point under 16
            while board['computer']['points'] < AGE:
                update_board(board, 'computer')
                print(board)
            return

        # Check if computer went over 21
        if check_over(board, 'computer'):
            return

        # Ask the player if player want to pick another card
        deal = input("Type 'y' to get another card, or  type 'n' to pass: ")

        if deal == 'y':
            update_board(board, 'player')
            print(f"Your cards: {board['player']['faces']}, current points: {board['player']['points']}.")

        else:  # deal == 'n'
            computer_continue(board)
            return



