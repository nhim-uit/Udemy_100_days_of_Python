from question_model import *


class QuizBrain:
    def __init__(self):
        self.__question_number = 0
        self.__question_list = QuestionBank()
        self.__score = 0

    def get_question(self):
        return self.__question_list.get_question(self.__question_number)

    def update_question(self):
        self.__question_number += 1

    def update_score(self):
        self.__score += 1

    def next_question(self):
        q = self.get_question()
        self.update_question()
        user_ans = input(f'Q.{self.__question_number}: {q.get_text()} (True/False)?: ')
        self.check_answer(user_ans, q.get_answer())

    def still_has_questions(self):
        return self.__question_number < self.__question_list.get_len()

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.update_score()
            print('You got it right!')
        else:
            print('That\'s wrong.')

        print(f'The correct answer was: {correct_ans}.')
        print(f'Your current score is: {self.__score}/{self.__question_number}.\n')

    def complete(self):
        print('*' * 30)
        print('You\'ve completed the quiz.')
        print(f'Your final score was: {self.__score}/{self.__question_number}.')
        print('*' * 30)
