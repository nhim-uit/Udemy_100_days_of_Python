# Udemy: Master Python by building 100 projects in 100 days
# Oct 4, 2024
# Day 27 - Miles to Km Converter
# Created by me

from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
# window.minsize(width=100, height=100)
window.config(padx=5, pady=20)

# Constants
FONT = ('Arial', 12, 'normal')

# Entry
text_box = Entry(window, width=10)
text_box.grid(column=1, row=0)

# label: miles
miles_lb = Label(text='Miles', font=FONT)
miles_lb.grid(column=2, row=0)

# label: is equal to
is_equal_to_lb = Label(text='is equal to', font=FONT)
is_equal_to_lb.grid(column=0, row=1)

# label: zero
zero_lb = Label(text='0', font=FONT)
zero_lb.grid(column=1, row=1)

# label: km
km_lb = Label(text='Km', font=FONT)
km_lb.grid(column=2, row=1)


# button
def button_click():
    km = round(int(text_box.get()) * 1.609)
    zero_lb.config(text=km)


button = Button(text='Calculate', command=button_click)
button.grid(column=1, row=2)

window.mainloop()
