# Udemy: Master Python by building 100 projects in 100 days
# Oct 26, 2024
# Day 33 - API
# Binance BTC Price API

import requests

response = requests.get(url='https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT')
response.raise_for_status()

data = response.json()
print(f"{float(data['price']):.2f}")
