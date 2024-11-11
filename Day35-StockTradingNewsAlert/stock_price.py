# functions

import os
import requests

from dotenv import load_dotenv
# from datetime import date

load_dotenv()

api_key = os.getenv('STOCK_PRICE_API')
# stock = 'AAPL'


# retrieve previous closing price
def get_prev_closing_price(stock):
    """
    :param stock: string
    :return: previous closing price: float
    """
    response_previous_close = (
        requests.get(f'https://api.polygon.io/v2/aggs/ticker/{stock}/prev?adjusted=true&apiKey={api_key}'))
    response_previous_close.raise_for_status()

    data = response_previous_close.json()
    prev_closing_price = data['results'][0]['c']
    # print(prev_closing_price)  # previous closing price

    return prev_closing_price


def get_today_closing_price(stock):
    """
    :param stock: string
    :return: today's closing price of stock: float
    """
    # today = date.today()
    today = '2024-11-08'

    response_daily_close = requests.get(f'https://api.polygon.io/v1/open-close/{stock}/{today}?adjusted=true&apiKey={api_key}')

    if response_daily_close.json()['status'] == 'OK':
        data1 = response_daily_close.json()
        # date = data1['from']
        closing_price = data1['close']
        # print(closing_price)

        return closing_price


def calc_percent(prev_price, today_price):
    """
    :param prev_price:
    :param today_price:
    :return: change percentage between two closing prices
    """
    percent = (today_price - prev_price) / prev_price * 100
    percent = round(percent, 2)
    return percent


# retrieve related news
def get_news(stock):
    """
    :param stock:
    :return: description of the news: string
    """
    news = requests.get(f'https://api.polygon.io/v2/reference/news?ticker={stock}&limit=10&apiKey={api_key}')
    news_data = news.json()
    title = news_data['results'][0]['title']
    description = news_data['results'][0]['description']
    # print(description)

    return title, description
