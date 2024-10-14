# Udemy: Master Python by building 100 projects in 100 days
# Oct 14, 2024
# Day 31 - Flash Card App - Capstone Project
# Created by me, with tutorials from the course

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flash Card :)')
window.config(width=1000, height=750, padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
wrong_img = PhotoImage(file='./images/wrong.png')
right_img = PhotoImage(file='./images/right.png')
card_font_img = PhotoImage(file='./images/card_front.png')

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(0, 0, anchor='nw', image=card_font_img)
text1 = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'), fill='black')
text2 = canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2, pady=50)

# buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0)
right_btn.grid(column=1, row=1)

window.mainloop()
