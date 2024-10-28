# Udemy: Master Python by building 100 projects in 100 days
# Oct 28, 2024
# Day 34 - GUI Quiz App
# Created by me

from quiz_brain import *
from tkinter import *
from PIL import Image, ImageTk
import random

#
q_bank = QuizBrain()
score = 0


# functions
def get_question():
    # print(q_bank.next_question())

    try:
        q = random.choice(q_bank.question_list)
        question = q.question
        answer = q.answer

        # canvas config
        question_id.config(text=question)
        q_bank.question_list.remove(q)

        return answer

    except IndexError:
        question_id.config(text='END')
        return 'The list is empty'


def press_true():
    answer_key = get_question()

    if answer_key.lower() == 'true':
        global score
        score += 1

        # config score label
        score_lb.config(text=f'Score: {score}')


# CONSTANTS
THEME_COLOR = "#375362"

# window
window = Tk()
window.title('Quiz App')
window.config(padx=20, pady=10, bg=THEME_COLOR)
window.geometry('250x300')

# label
score_lb = Label(text='Score: 0', bg=THEME_COLOR,
                 fg='white',
                 font=('Arial', 10, 'normal'))
# score_lb.config(pady=20)
score_lb.grid(column=1, row=0, sticky='e')

# canvas
# canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
# question_id = canvas.create_text(100, 100, text='Question goes here',
#                    fill='black',
#                    font=('Arial', 12, 'italic'))
# canvas.grid(column=0, row=1, columnspan=2, pady=20)

# message
question_id = Label(text='Question goes here', wraplength=200)
question_id.grid(column=0, row=1, columnspan=2, pady=20, sticky='nsew')

# images
true_img = Image.open('./images/true.png')
resized_true_img = true_img.resize((50, 50))
true_photo = ImageTk.PhotoImage(resized_true_img)
false_img = Image.open('./images/false.png')
resized_false_img = false_img.resize((50, 50))
false_photo = ImageTk.PhotoImage(resized_false_img)

# buttons
true_btn = Button(image=true_photo,
                  highlightthickness=0,
                  command=press_true)
true_btn.grid(column=0, row=2)

false_btn = Button(image=false_photo,
                  highlightthickness=0)
false_btn.grid(column=1, row=2)

# get question
get_question()

# fix the size of the row and column
window.grid_rowconfigure(0, weight=0)
# window.grid_columnconfigure(0, weight=1)

# set fixed size for the row and column
question_id.grid_propagate(False)
question_id.config(width=30, height=10)

window.mainloop()
