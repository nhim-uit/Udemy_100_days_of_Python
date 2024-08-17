import random
from data import *


def choices():
    """
    randomly choose 2 data to compare
    :return: list
    """
    return random.sample(data, 2)


def compare(datas: list, player: str):
    """
    Take the user's guess and the follower counts and return if they got it right.
    :param datas:
    :param player:
    :return:
    """
    count1 = datas[0]['follower_count']
    count2 = datas[1]['follower_count']

    # result of comparing two data's follower counts
    if count1 > count2:
        flag = 'A'
    else:  # count1 < count2:
        flag = 'B'

    # compare resulted followers comparison with user input
    if player.upper() == flag:
        return True
    else:
        return False


def print_data(data: dict):
    """
    Takes the data and returns the printable format.
    :param data: dictionary
    :return: string
    """
    return f"{data['name']}, a {data['description']}, from {data['country']}."


def run():
    running = True
    score = 0

    while running:
        # randomly pick two people from data
        datas = choices()
        data1 = datas[0]
        data2 = datas[1]

        # print out data picked
        print(f'Compare A: {print_data(data1)}')
        print(f'Against B: {print_data(data2)}')

        # ask user for their choice
        choice = input('Who has more followers? Type \'A\' or \'B\': ')

        # compare follower counts and user's input
        win = compare(datas, choice)

        # print out result
        if win:
            score += 1
            print(f'You\'re right! Current score: {score}.')
        else:
            print(f'Sorry, that\'s wrong. Final score: {score}.')
            running = False






