# Udemy: Master Python by building 100 projects in 100 days
# Oct 26, 2024
# Day 33 - API
# Sunrise sunset API

import requests
from datetime import datetime
import pytz

# Ho Chi Minh City
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
sunrise_utc = data['results']['sunrise']
sunset_utc = data['results']['sunset']

# Convert to datetime objects
sunrise_utc = datetime.fromisoformat(sunrise_utc.replace("Z", "+00:00"))
sunset_utc = datetime.fromisoformat(sunset_utc.replace("Z", "+00:00"))

# Convert from UTC to Indochina Time (ICT)
ict_timezone = pytz.timezone("Asia/Bangkok")  # ICT is UTC+7
sunrise_ict = sunrise_utc.astimezone(ict_timezone)
sunset_ict = sunset_utc.astimezone(ict_timezone)

# get current hour
time_now_hour = datetime.now().hour
# print(time_now_hour)
