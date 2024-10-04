# Udemy: Master Python by building 100 projects in 100 days
# Oct 2nd, 2024
# Day 27 - Tkinter

from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# label
label = Label(text='I Am a Label', font=('Arial', 24, 'bold'))
# label.pack(expand=True)  # display on screen
label.pack()
# default to side = 'top'
# label.pack(side='bottom')
# label.pack(side='left')

label['text'] = 'new text'
label.config(text='New text 1')


# button
def button_clicked():
    print('I got clicked')
    new_text = input.get()
    label.config(text=new_text)


button = Button(text='Click me', command=button_clicked)
button.pack()


# entry
input = Entry(width=10)
input.pack()


window.mainloop()
