# Udemy: Master Python by building 100 projects in 100 days
# Aug 06-08, 2024
# Day 11 - Blackjack Capstone Project
# Created by me
# Version 1: no graphic

from run import run

if __name__ == '__main__':
    # Driver of multiple Black Jack games
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

    while play == 'y':
        run()

        print('-' * 50)
        play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
        print('-' * 50)

    print('Bye!!!')


