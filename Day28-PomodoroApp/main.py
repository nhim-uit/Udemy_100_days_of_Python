# Udemy: Master Python by building 100 projects in 100 days
# Oct 7, 2024
# Day 28 - Pomodoro App
# Created by me
# Version 1: timer counting forward, start at 00:00 to 25:00

from tkinter import *
from Timer import *
from CONSTANTS import *


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    timer.reset(canvas, text_id, check_mark_lb, title_lb)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start():
    timer.start(check_mark_lb, title_lb)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# label - title
title_lb = Label(text='Timer', font=(FONT_NAME, 30, 'normal'))
title_lb.config(bg=YELLOW, fg=GREEN)
title_lb.grid(column=1, row=0)

# label - check_mark
# ✔
check_mark_lb = Label(text='', font=(FONT_NAME, 15, 'bold'))
check_mark_lb.config(bg=YELLOW, fg=GREEN)
check_mark_lb.grid(column=1, row=2)

# button - Start
start_btn = Button(text='Start', command=start)
start_btn.config(bg='white')
start_btn.grid(column=0, row=2)

# button - Reset
reset_btn = Button(text='Reset', command=reset)
reset_btn.config(bg='white')
reset_btn.grid(column=2, row=2)

# timer
timer = Timer(canvas, text_id, window)

window.mainloop()
