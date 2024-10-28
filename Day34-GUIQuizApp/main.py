# Udemy: Master Python by building 100 projects in 100 days
# Oct 28, 2024
# Day 34 - GUI Quiz App
# Created by me

from quiz_brain import *

if __name__ == '__main__':
    q_bank = QuizBrain()

    while q_bank.still_has_questions():
        q_bank.next_question()

    q_bank.complete()
