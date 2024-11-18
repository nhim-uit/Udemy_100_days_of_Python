# Udemy: Master Python by building 100 projects in 100 days
# Nov 11-18, 2024
# Day 36 - Stock Trading News Alert
# Created by me

from stock_price import *
from send_sms import *

if __name__ == '__main__':
    stock = 'TSLA'  # Tesla stock

    prev_price, today_price = get_closing_prices(stock)

    print(prev_price)
    print(today_price)

    change = calc_percent(prev_price, today_price)
    print(f'change: {change}%')

    if change > 0:
        emoji = '🔺'
    else:
        emoji = '🔻'

    if abs(change) > 1:
        title, description = get_news(stock)

        message = client.messages.create(
            body=f'{stock}: {emoji}{change}%\n{title}\n{description}',
            from_=os.getenv('TWILIO_NUMBER'),
            to=os.getenv('MY_VIRTUAL_PHONE_NUMBER'),
        )

        print('Get News')
        print(message.status)

