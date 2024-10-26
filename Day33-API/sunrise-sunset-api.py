# Udemy: Master Python by building 100 projects in 100 days
# Oct 26, 2024
# Day 33 - API
# Sunrise sunset API

import requests
from datetime import datetime

MY_LAT = 10.823099
MY_LONG = 106.629662

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

response = requests.get(' https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise.split('T')[1])
print(sunset.split('T')[1])

time_now = datetime.now()
