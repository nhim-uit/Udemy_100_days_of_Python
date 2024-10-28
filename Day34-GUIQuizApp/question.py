from data import *
import html


class Question:
    def __init__(self, question, answer):
        self.__question = html.unescape(question)
        self.__answer = answer

    @property
    def question(self):
        return self.__question

    @property
    def answer(self):
        return self.__answer


class QuestionBank:
    def __init__(self):
        self.__question_bank = []

        for q in data['results']:
            self.__question_bank.append(Question(q['question'], q['correct_answer']))

        self.__len = len(self.__question_bank)
        self.__number = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        self.__number = val

    @property
    def question_bank(self):
        return self.__question_bank

    @property
    def question_bank_question(self):
        # return Object Question
        return self.__question_bank[self.number]

    @property
    def len(self):
        return self.__len

    def remove_question(self, question, correct_answer):
        self.__question_bank.remove(Question(question, correct_answer))
