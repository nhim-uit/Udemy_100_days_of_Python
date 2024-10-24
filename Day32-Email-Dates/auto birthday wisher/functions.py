import datetime as dt
import random
from email.mime.text import MIMEText
import smtplib
import pandas


def get_df(filename):
    # open file to read
    try:
        df = pandas.read_csv(filename)
    except FileNotFoundError:
        print(f'{filename} file not found')
        return

    return df


def get_day_month():
    return dt.datetime.now().day, dt.datetime.now().month


def get_letter_content(row):
    # randomly choose a letter template
    letter_no = random.randint(1, 3)
    template_file = f'letter_{letter_no}.txt'

    # read template file and replace name
    try:
        with open(template_file, 'r') as template:
            letter_content = template.read()
    except FileNotFoundError:
        print(f'{template_file} not found')

    return letter_content.replace('[NAME]', row['name'])


def create_email_msg(new_letter, my_email, recipient_email):
    msg = MIMEText(new_letter, 'plain', 'utf-8')
    msg['Subject'] = 'Happy Birthday!'
    msg['From'] = my_email
    msg['To'] = recipient_email
    return msg


def send_email(my_email, my_password, recipient_email, msg):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=msg.as_string())

    # print('Email sent successfully')
