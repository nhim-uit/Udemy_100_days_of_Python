# Udemy: Master Python by building 100 projects in 100 days
# Oct 2nd, 2024
# Day 27 - Tkinter

from tkinter import *

from sqlalchemy import column

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
label = Label(text='I Am a Label', font=('Arial', 24, 'bold'))
# label.pack(expand=True)  # display on screen
# label.pack()
# default to side = 'top'
# label.pack(side='bottom')
# label.pack(side='left')
# label.place(x=0, y=0)
label.grid(column=0, row=0)

label['text'] = 'new text'
label.config(text='New text 1')
label.config(padx=50, pady=50)


# button
def button_clicked():
    print('I got clicked')
    new_text = input1.get()
    label.config(text=new_text)


button = Button(text='Click me', command=button_clicked)
# button.pack(side='left')
button.grid(column=1, row=1)

button1 = Button(text='New Button')
button1.grid(column=2, row=0)

# entry
input1 = Entry(width=10)
# input1.pack(side='left')
input1.grid(column=3, row=2)

window.mainloop()
