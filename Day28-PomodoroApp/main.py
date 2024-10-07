# Udemy: Master Python by building 100 projects in 100 days
# Oct 7, 2024
# Day 28 - Pomodoro App
# UI, timer reset, timer mechanism created by me

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start():
    pass

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.pack()

# label - Timer
timer_lb = Label(text='Timer', font=(FONT_NAME, 30, 'normal'))
timer_lb.config(bg=YELLOW, fg=GREEN)
timer_lb.place(x=40, y=-40)

# button - Start
start_btn = Button(text='Start', command=start)
start_btn.config(bg='white')
start_btn.place(x=-40, y=200)

# button - Reset
reset_btn = Button(text='Reset', command=reset)
reset_btn.config(bg='white')
reset_btn.place(x=200, y=200)

window.mainloop()
