# Udemy: Master Python by building 100 projects in 100 days
# Oct 14-16, 2024
# Day 31 - Flash Card App - Capstone Project
# Created by me, with tutorials from the course

from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# load data
# filename = 'cleaned_data.csv'
filename = 'example_data.csv'
words_to_learn_file = 'words_to_learn.csv'


# functions
def get_word():
    global random_card, df, flip_timer

    # open data file
    try:
        df = pandas.read_csv(words_to_learn_file, index_col=False)

        if df.empty:
            canvas.itemconfig(title, text='Congrats!!!', fill='black')
            canvas.itemconfig(word, text='DONE', fill='black')
            return

    except FileNotFoundError:
        df = pandas.read_csv(filename, index_col=False)

    data_dict = df.to_dict(orient='records')  # list of dict, [{column->value}]

    # cancel auto wait 3ms until flip 1 card and wait
    window.after_cancel(flip_timer)

    # get random word
    random_card = random.choice(data_dict)
    random_word = random_card.get('Vietnamese')

    # canvas config
    canvas.itemconfig(img, image=card_front_img)
    canvas.itemconfig(title, text='Vietnamese', fill='black')
    canvas.itemconfig(word, text=random_word, fill='black')

    # auto flip
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(img, image=card_back_img)
    canvas.itemconfig(title, fill='white', text='English')
    canvas.itemconfig(word, fill='white', text=random_card.get('English'))


def write_words_to_learn():
    get_word()

    filtered_df = df[~df['Vietnamese'].str.fullmatch(random_card['Vietnamese'],
                                            case=False, na=False)]
    filtered_df.to_csv(words_to_learn_file, index=False, encoding='utf-8')


# window
window = Tk()
window.title('Flash Card :)')
window.config(width=1000, height=750, padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
wrong_img = PhotoImage(file='./images/wrong.png')
right_img = PhotoImage(file='./images/right.png')
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')

# window reload
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img = canvas.create_image(0, 0, anchor='nw', image=card_front_img)
title = canvas.create_text(400, 150, text='Flip Card Game',
                        font=('Arial', 40, 'italic'), fill='black')
word = canvas.create_text(400, 263, text='Let\'t get started',
                        font=('Arial', 60, 'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2, pady=50)

# buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0,
                   borderwidth=0, command=get_word)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0,
                   borderwidth=0, command=write_words_to_learn)
right_btn.grid(column=1, row=1)

# calls get_word to generate viet word
get_word()

window.mainloop()
