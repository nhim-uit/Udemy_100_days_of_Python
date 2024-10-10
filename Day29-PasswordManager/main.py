# Udemy: Master Python by building 100 projects in 100 days
# Oct 10, 2024
# Day 29 - Password Manager App with Tkinter
# Created by me

from tkinter import *

from CONSTANTS import *

# window
window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=30)

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
bg_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=0, row=0, columnspan=3)

# labels
website_lb = Label(text='Website:', font=FONT)
website_lb.grid(column=0, row=1)

email_lb = Label(text='Email/Username:', font=FONT)
email_lb.grid(column=0, row=2)

password_lb = Label(text='Password:', font=FONT)
password_lb.grid(column=0, row=3)

# button
gen_pass_btn = Button(text='Generate Password')
gen_pass_btn.grid(column=2, row=3, padx=(50, 0))

add_btn = Button(text='Add')
add_btn.grid(column=1, row=4, columnspan=2, sticky='ew', pady=2)
# use sticky='ew' to span all its grid cell

# entry
website_entry = Entry(window, font=FONT)
website_entry.grid(column=1, row=1, columnspan=2, sticky='ew', pady=2)

email_entry = Entry(window, font=FONT)
email_entry.grid(column=1, row=2, columnspan=2, sticky='ew', pady=2)

password_entry = Entry(window, font=FONT)
password_entry.grid(column=1, row=3, sticky='ew', pady=2)

# prefilled info for email entry
email_entry.insert(0, 'alex@gmail.com')

window.mainloop()
