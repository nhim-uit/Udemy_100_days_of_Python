# Udemy: Master Python by building 100 projects in 100 days
# Oct 26, 2024
# Day 32 - Send Emails

import smtplib

my_email = 'alex.test.app.7@gmail.com'
my_password = 'dvhuulpnkkpfkwts'


def send_email():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='alexisfun065@gmail.com',
                            msg='Subject:ISS Is Close\n\nLook up!')
