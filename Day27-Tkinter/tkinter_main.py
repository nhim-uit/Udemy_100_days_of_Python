# Udemy: Master Python by building 100 projects in 100 days
# Oct 2nd, 2024
# Day 27 - Tkinter

import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# label
label = tkinter.Label(text='I Am a Label', font=('Arial', 24, 'bold'))
label.pack(expand=True)  # display on screen
# default to side = 'top'
# label.pack(side='bottom')
# label.pack(side='left')


window.mainloop()
