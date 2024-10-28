from question import *


class QuizBrain:
    def __init__(self):
        self.__question_number = 0
        self.__question_list = QuestionBank()
        self.__score = 0

    @property
    def question_number(self):
        return self.__question_number

    @property
    def question(self):
        self.__question_list.number = self.__question_number
        return self.__question_list.question_bank_question

    @property
    def question_list(self):
        return self.__question_list.question_bank

    @property
    def score(self):
        return self.__score

    def update_question(self):
        self.__question_number += 1

    def update_score(self):
        self.__score += 1

    def next_question(self):
        q = self.question
        self.update_question()

        # user_ans = input(f'Q.{self.__question_number}: {q.question} (True/False)?: ')
        # self.check_answer(user_ans, q.answer)

        return q

    def still_has_questions(self):
        return self.__question_number < self.__question_list.len

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.update_score()
            # print('You got it right!')
            return True
        else:
            # print('That\'s wrong.')
            return False

        # print(f'The correct answer was: {correct_ans}.')
        # print(f'Your current score is: {self.__score}/{self.__question_number}.\n')

    def complete(self):
        print('*' * 27)
        print('You\'ve completed the quiz.')
        print(f'Your final score was: {self.__score}/{self.__question_number}.')
        print('*' * 27)
