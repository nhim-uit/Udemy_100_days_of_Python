# Udemy: Master Python by building 100 projects in 100 days
# Nov 11, 2024
# Day 36 - Stock Trading News Alert
# Created by me

from stock_price import *

if __name__ == '__main__':
    stock = 'AAPL'  # Apple, Inc. stock

    prev_price = get_prev_closing_price(stock)
    today_price = get_today_closing_price(stock)

    change = calc_percent(prev_price, today_price)

    print(f'change: {change}%')
    print(f'{get_news(stock)}')
