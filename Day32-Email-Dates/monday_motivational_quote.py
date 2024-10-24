# Udemy: Master Python by building 100 projects in 100 days
# Oct 24, 2024
# Day 32 - Monday motivational quotes

import datetime as dt
import smtplib
import random
from email.mime.text import MIMEText

# email info
my_email = 'alex.test.app.7@gmail.com'
my_password = 'dvhuulpnkkpfkwts'
recipient_email = 'alexisfun065@gmail.com'

# datetime
now = dt.datetime.now()
day_of_week = now.weekday()

# open quotes file to choose
try:
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
        quote = random.choice(quotes).strip()
except FileNotFoundError as e:
    print(e)

# create the email message
msg = MIMEText(quote, 'plain', 'utf-8')
msg['Subject'] = 'Monday Motivational Quote'
msg['From'] = my_email
msg['To'] = recipient_email

# if it's Monday, send the email
if day_of_week == 0:    # 0 is Monday
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=msg.as_string())

    print('Email sent successfully')
