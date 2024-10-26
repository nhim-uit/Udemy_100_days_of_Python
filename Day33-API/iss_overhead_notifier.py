# Udemy: Master Python by building 100 projects in 100 days
# Oct 26, 2024
# Day 33 - API
# ISS Overhead Notifier Project
import time

from sunrise_sunset_api import *
from send_email import *

MY_LAT = 10.823099
MY_LONG = 106.629662

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

# print(iss_latitude)
# print(iss_longitude)

# If the ISS is close to my current position,
# and it is currently dark
# then send an email to tell me to look up
# BONUS: run the code every 60 seconds -- use pythonanywhere

while True:
    time.sleep(60)
    if abs(iss_latitude - MY_LAT) <= 5 \
            and abs(iss_longitude - MY_LONG) <= 5 \
            and (time_now_hour <= sunrise_ict.hour
                 or time_now_hour >= sunset_ict.hour):
        send_email()
