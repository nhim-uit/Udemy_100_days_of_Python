# Udemy: Master Python by building 100 projects in 100 days
# Oct 24, 2024
# Day 32 - Automated Birthday Wisher
# Created by me

import pandas
import random
import datetime as dt
import smtplib
from email.mime.text import MIMEText

# email info
my_email = 'alex.test.app.7@gmail.com'
my_password = 'dvhuulpnkkpfkwts'

# datetime
now = dt.datetime.now()
target_day = now.day
target_month = now.month

# list of birthdays
birthday_list = 'birthday.csv'

# open file to read
try:
    df = pandas.read_csv(birthday_list)
except FileNotFoundError:
    print(f'{birthday_list} file not found')

# find matching birthday
matching_rows = df[(df['day'] == target_day) & (df['month'] == target_month)]

# iterate through df matching birthdays
for index, row in matching_rows.iterrows():
    # randomly choose a letter template
    letter_no = random.randint(1, 3)
    template_file = f'letter_{letter_no}.txt'
    print(template_file)

    # read template file and replace name
    try:
        with open(template_file, 'r') as template:
            letter_content = template.read()
    except FileNotFoundError as e:
        print(f'{template_file} not found')

    new_letter = letter_content.replace('[NAME]', row['name'])
    # print(new_letter)

    recipient_email = row['email']

    # create the email message
    msg = MIMEText(new_letter, 'plain', 'utf-8')
    msg['Subject'] = 'Happy Birthday!'
    msg['From'] = my_email
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=msg.as_string())

    print('Email sent successfully')
