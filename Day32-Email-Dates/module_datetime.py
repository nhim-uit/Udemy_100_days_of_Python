# Udemy: Master Python by building 100 projects in 100 days
# Oct 24, 2024
# Day 32 - Datetime module

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

# print(day_of_week)

date_of_birth = dt.datetime(year=1994, month=10, day=16, hour=4)
print(date_of_birth)
