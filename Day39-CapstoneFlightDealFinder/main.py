# Udemy: Master Python by building 100 projects in 100 days
# Nov 21 - Dec 03, 2024
# Day 39 - Capstone Project: Flight Deal Finder
# APIs used:
# Amadeus Flight Search API: https://developers.amadeus.com/
# Sheety API
# Twilio Messaging API
# Cannot sign up for Amadeus Flight Search API
# sample solution: using OOP

import time
from data_manager import DataManager
from flight_search import FlightSearch

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
flight_search = FlightSearch()

# ==================== Update the Airport Codes in Google Sheet ====================

#  In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the API.
#  You should use the code you get back to update the sheet_data dictionary.

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

