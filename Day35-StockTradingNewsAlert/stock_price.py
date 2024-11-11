import os
import requests

from dotenv import load_dotenv
# from datetime import date

load_dotenv()

api_key = os.getenv('STOCK_PRICE_API')
stock = 'AAPL'

# retrieve previous closing price
response_previous_close = (
    requests.get(f'https://api.polygon.io/v2/aggs/ticker/{stock}/prev?adjusted=true&apiKey={api_key}'))
response_previous_close.raise_for_status()

data = response_previous_close.json()
prev_closing_price = data['results'][0]['c']
print(prev_closing_price)  # previous closing price

