from tkinter import *
from quiz_brain import *
from tkinter import *
from PIL import Image, ImageTk
import random


# CONSTANTS
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.__quiz_brain = quiz_brain
        self.__score = 0

        # window
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=10, bg=THEME_COLOR)
        self.window.geometry('250x300')

        # label
        self.score_lb = Label(text='Score: 0', bg=THEME_COLOR,
                         fg='white',
                         font=('Arial', 10, 'normal'))
        # score_lb.config(pady=20)
        self.score_lb.grid(column=1, row=0, sticky='e')

        # canvas
        # canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
        # question_id = canvas.create_text(100, 100, text='Question goes here',
        #                    fill='black',
        #                    font=('Arial', 12, 'italic'))
        # canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # message
        self.question_id = Label(text='Question goes here', wraplength=200)
        self.question_id.grid(column=0, row=1, columnspan=2, pady=20, sticky='nsew')

        # images
        self.true_img = Image.open('./images/true.png')
        self.resized_true_img = self.true_img.resize((50, 50))
        self.true_photo = ImageTk.PhotoImage(self.resized_true_img)
        self.false_img = Image.open('./images/false.png')
        self.resized_false_img = self.false_img.resize((50, 50))
        self.false_photo = ImageTk.PhotoImage(self.resized_false_img)

        # buttons
        self.true_btn = Button(image=self.true_photo,
                          highlightthickness=0,
                          command=lambda: self.press('true'))
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=self.false_photo,
                           highlightthickness=0,
                           command=lambda: self.press('false'))
        self.false_btn.grid(column=1, row=2)

        # get question
        self.get_question()

        # fix the size of the row and column
        self.window.grid_rowconfigure(0, weight=0)
        # window.grid_columnconfigure(0, weight=1)

        # set fixed size for the row and column
        self.question_id.grid_propagate(False)
        self.question_id.config(width=30, height=10)

        self.window.mainloop()

    # functions
    def get_question(self):
        # print(q_bank.next_question())

        try:
            q = self.__quiz_brain.next_question()
            question = q.question
            answer = q.answer

            # canvas config
            self.question_id.config(text=question)
            self.__quiz_brain.question_list.remove(q)

            print(self.__quiz_brain.question_list)

            return answer

        except IndexError:
            self.question_id.config(text='END')
            print('empty list')
            return 'The list is empty'

    def press(self, key):
        answer_key = self.get_question()

        if answer_key.lower() == key:
            self.__score += 1

            # config score label
            self.score_lb.config(text=f'Score: {self.__score}')
