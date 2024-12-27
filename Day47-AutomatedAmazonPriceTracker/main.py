# Udemy: Master Python by building 100 projects in 100 days
# Dec 25, 2024
# Day 47 - an Automated Amazon Price Tracker
# Created by me
from dbm import error

from functions import *
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

BUY_PRICE = 70

if __name__ == '__main__':
    url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
    response_text = get_response(url)
    try:
        price = get_price(response_text)
    except Exception as e:
        print(f'cannot get price: {e}')
        price = None
    try:
        title = get_title(response_text)
    except Exception as e:
        print(f'cannot get title: {e}')
        title = 'Unknown product'

    if price is not None and price >= BUY_PRICE:
        message = f'{title} is on sale for {price}'

        send_email(sender_email=SENDER_EMAIL,
                   sender_password=SENDER_PASSWORD,
                   recipient_email=RECIPIENT_EMAIL,
                   subject='PRICE DROP ALERT!!!',
                   body=message)
