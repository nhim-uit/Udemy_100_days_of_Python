from data import *


class Question:
    def __init__(self, text, answer):
        self.__text = text
        self.__answer = answer

    def get_text(self):
        return self.__text

    def get_answer(self):
        return self.__answer


class QuestionBank:
    def __init__(self):
        self.__question_bank = []

        for q in question_data:
            self.__question_bank.append(Question(q['text'], q['answer']))

        self.__len = len(self.__question_bank)

    def get_question(self, number):
        # return Object Question
        return self.__question_bank[number]

    def get_len(self):
        return self.__len
