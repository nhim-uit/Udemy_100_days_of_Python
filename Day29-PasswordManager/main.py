# Udemy: Master Python by building 100 projects in 100 days
# Oct 10, 2024
# Day 29-30 - Password Manager App with Tkinter
# Created by me

import pandas
import pyperclip    # to copy and paste to clipboard
import json

from tkinter import *
from tkinter import messagebox

from CONSTANTS import *
from random_password import generate_random_password


# functions
def generate_password():
    password_entry.delete(0, END)
    password = generate_random_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)    # copy generated password to clipboard


def save_using_csv():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty! ')
    else:
        is_ok = messagebox.showinfo(title=website, message=f"These are the details entered:\n"
                                                           f"Website: {website}\n"
                                                           f"Email: {email}\n"
                                                           f"Password: {password}\n"
                                                           f"Is it ok to save?")
        if is_ok:
            filename = 'data.csv'
            new_row = {'website': website,
                       'email': email,
                       'password': password,
                       }
            new_row_df = pandas.DataFrame([new_row])

            try:
                pandas.read_csv(filename)
                new_row_df.to_csv(filename, mode='a', index=False, header=False)
            except FileNotFoundError:
                pandas.DataFrame(columns=['website', 'email', 'password'])
                new_row_df.to_csv(filename, mode='a', index=False)

            # messagebox.showinfo(title='Success', message=f'Added {website} to the datastore.')

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, 'alex@gmail.com')
            password_entry.delete(0, END)


def save_using_json():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty! ')
    else:
        filename = 'data.json'
        new_data = {
            website: {
                'email': email,
                'password': password,
            }
        }

        try:
            with open(filename, 'r') as file:
                # write new json to file
                # json.dump(new_data, file, indent=4)

                # reading old data
                data = json.load(file)

                # updating old data with new data
                data.update(new_data)

            with open(filename, 'w') as file:
                # save updated data
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open(filename, 'w') as file:
                json.dump(new_data, file, indent=4)

        # clear all entry
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, 'alex@gmail.com')
        password_entry.delete(0, END)


def search_using_csv():
    filename = 'data.csv'

    df = pandas.read_csv(filename)

    search_website = website_entry.get()
    search_email = email_entry.get()

    if len(search_website) == 0 or len(search_email) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave website or email field empty! ')
    else:
        result = df[(df['website'] == search_website) & (df['email'] == search_email)]

        if result.empty:
            messagebox.showinfo(title='Oops!', message=f'No found password for {search_website} and {search_email}')
        else:
            messagebox.showinfo(title='Found!', message=f'Website: {search_website}\n'
                                                        f'Email: {search_email}\n'
                                                        f'Password: {result.password.item()}')


def search_using_json():
    filename = 'data.json'

    search_website = website_entry.get()
    search_email = email_entry.get()

    if len(search_website) == 0 or len(search_email) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave website or email field empty! ')
    else:
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

                if search_website in data:
                    if data[search_website].get('email') == search_email:
                        messagebox.showinfo(title='Found!',
                                            message=f'Website: {search_website}\n'
                                                    f"Email: {search_email}\n"
                                                    f"Password: {data[search_website]['password']}")
                    else:
                        messagebox.showinfo(title='Oops!',
                                            message=f'No found password for {search_website} and {search_email}')
                else:
                    messagebox.showinfo(title='Oops!',
                                        message=f'{search_website} has no password.')
        except FileNotFoundError:
            messagebox.showinfo(title='Oops!', message=f'Database is empty.')


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
gen_pass_btn = Button(text='Generate Password', command=generate_password)
gen_pass_btn.grid(column=2, row=3, padx=(10, 0))

add_btn = Button(text='Add', command=save_using_json)
add_btn.grid(column=1, row=4, columnspan=2, sticky='ew', pady=2)
# use sticky='ew' to span all its grid cell

search_btn = Button(text='Search', command=search_using_json)
search_btn.grid(column=2, row=1, sticky='ew', pady=2, padx=(10, 0))

# entry
website_entry = Entry(window, font=FONT)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky='ew', pady=2)

email_entry = Entry(window, font=FONT)
email_entry.grid(column=1, row=2, columnspan=2, sticky='ew', pady=2)

password_entry = Entry(window, font=FONT)
password_entry.grid(column=1, row=3, sticky='ew', pady=2)

# prefilled info for email entry
email_entry.insert(0, 'alex@gmail.com')

window.mainloop()
