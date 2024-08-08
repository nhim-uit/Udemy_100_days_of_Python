import random
from CONSTANTS import *


def start():
    """
    Print welcome and return number of attempts
    :return: int, number of attempts
    """
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    mode = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    return EASY if mode == 'easy' else HARD


def compare(number: int, guess: int):
    """
    Compare number created and guess from player
    Return flag
    :param number: number randomly created
    :param guess: from player
    :return: boolean
    """
    if number > guess:
        print('Too low.')
        return False
    elif number < guess:
        print('Too high.')
        return False
    else:
        print(f'You got it! The answer was {guess}.')
        return True


def run():
    """
    Run the game
    :return: void
    """
    number = random.randint(1, 100)
    attempt = start()

    while attempt > 0:
        print(f'You have {attempt} attempts remaining to guess the number.')

        guess = int(input('Make a guess: '))
        right = compare(number, guess)

        if not right:
            attempt -= 1

            if attempt == 0:
                print(f'You lost. The number was {number}.')
                return

            print('Guess again.')
        else:
            return


