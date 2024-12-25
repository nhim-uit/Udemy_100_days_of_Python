# Udemy: Master Python by building 100 projects in 100 days
# Dec 25, 2024
# Day 47 - an Automated Amazon Price Tracker
# Created by me

from functions import *
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

BUY_PRICE = 100

if __name__ == '__main__':
    url = 'https://appbrewery.github.io/instant_pot/'
    response_text = get_response(url)
    price = get_price(response_text)
    title = get_title(response_text)

    if price >= BUY_PRICE:
        message = f'{title} is on sale for {price}'

        send_email(sender_email=SENDER_EMAIL,
                   sender_password=SENDER_PASSWORD,
                   recipient_email=RECIPIENT_EMAIL,
                   subject='PRICE DROP ALERT!!!',
                   body=message)
