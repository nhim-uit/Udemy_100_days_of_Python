import random
from deck import deck


def convert(face: str):
    val = face[1:]
    if val == 'A':
        return 11
    elif val == 'J' or val == 'Q' or val == 'K':
        return 10
    else:
        return int(val)


def calc_pts(faces: list):
    s = 0
    for i in faces:
        s += convert(i)

    return s


def create(player: list, computer: list):
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
    chosen_card = random.sample(deck, 1)
    #chosen_card = ['SA']

    deck.remove(chosen_card[0])
    board[player]['faces'].extend(chosen_card)

    new_pts = calc_pts(chosen_card)
    cur_pts = board[player]['points']

    board[player]['points'] += new_pts

    update_aces(board, player)


def update_aces(board: dict, player: str):
    faces = board[player]['faces']
    aces = [i[1:] for i in faces]

    if 'A' in aces and board[player]['points'] > 21:
        for i in range(len(faces)):
            if aces[i] == 'A':
                board[player]['faces'][i] = board[player]['faces'][i].replace('A', '1')

    board[player]['points'] = calc_pts(faces)


def update_deck(cards: list):
    for card in cards:
        deck.remove(card)


def check_win(board: dict):
    player_pts = board['player']['points']
    cmpt_pts = board['computer']['points']

    if cmpt_pts > 21 and player_pts > 21:
        return 'draw'
    elif cmpt_pts > 21:
        return 'win'
    elif player_pts > 21:
        return 'lose'
    else:
        if cmpt_pts < player_pts:
            return 'win'
        elif cmpt_pts == player_pts:
            return 'draw'
        else:
            return 'lose'


def check_over(board: dict, player: str):
    if board[player]['points'] > 21:
        return True

    return False


def check_bj(board: dict, player: str):
    if board[player]['points'] == 21:
        return True

    return False


def computer_continue(board):
    while board['computer']['points'] <= 21 \
            and board['computer']['points'] < board['player']['points'] \
            or board['computer']['points'] < 16:
        update_board(board, 'computer')
        print(board)


def print_res(board):
    res = check_win(board)
    if res == 'win':
        print(f"Player wins with {board['player']['points']} points.")
    elif res == 'lose':
        print(f"Computer wins with {board['computer']['points']} points.")
    elif res == 'draw':
        print(f"Player and computer draw with: "
              f"player ({board['player']['points']} pts), " 
              f"computer ({board['computer']['points']} pts).")

    print(f"Computer's faces: {board['computer']['faces']}. ")


def drive(board):
    done = False

    while not done:
        if check_bj(board, 'player') or check_bj(board, 'computer'):
            return
        if check_over(board, 'player'):
            while board['computer']['points'] < 16:
                update_board(board, 'computer')
                print(board)
            return
        if check_over(board, 'computer'):
            return

        deal = input("Type 'y' to get another card, or  type 'n' to pass: ")

        if deal == 'y':
            update_board(board, 'player')
            print(f"Your cards: {board['player']['faces']}, current points: {board['player']['points']}.")

        else:
            computer_continue(board)
            return



