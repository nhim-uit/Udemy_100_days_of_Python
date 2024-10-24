# Udemy: Master Python by building 100 projects in 100 days
# Oct 24, 2024
# Day 32 - Automated Birthday Wisher
# Created by me

from functions import *

# email info
my_email = 'alex.test.app.7@gmail.com'
my_password = 'dvhuulpnkkpfkwts'

# datetime
target_day, target_month = get_day_month()

# list of birthdays
birthday_list = 'birthday.csv'
df = get_df(birthday_list)

# find matching birthday
matching_rows = df[(df['day'] == target_day) & (df['month'] == target_month)]

# iterate through df matching birthdays
for index, row in matching_rows.iterrows():
    new_letter = get_letter_content(row)

    # get recipient email
    recipient_email = row['email']

    # create the email message
    msg = create_email_msg(new_letter, my_email, recipient_email)

    # send email
    send_email(my_email, my_password, recipient_email, msg)



