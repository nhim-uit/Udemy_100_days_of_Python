# Udemy: Master Python by building 100 projects in 100 days
# Aug 20-21, 2024
# Day 17 - Quiz Project
# My version: OOP with encapsulation
# API used: opentdb.com
# no abstraction, no inheritance, no polymorphism
# no try catch
# no docstrings

from quiz_brain import *

if __name__ == '__main__':
    q_bank = QuizBrain()

    while q_bank.still_has_questions():
        q_bank.next_question()

    q_bank.complete()
