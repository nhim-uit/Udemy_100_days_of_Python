# Udemy: Master Python by building 100 projects in 100 days
# Nov 19, 2024
# Day 38 - Working Out Tracking Using Google Sheets

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# NUTRITIONIX NPL EXERCISES API
NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('Tell me which exercises you did: ')

nutritionix_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
}

nutritionix_params = {
    'query': exercise_text,
    'weight_kg': os.getenv('WEIGHT'),
    'height_cm': os.getenv('HEIGHT'),
    'age': os.getenv('AGE'),
}

responses = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
result = responses.json()
print(result['exercises'][0]['name'])
print(result['exercises'][0]['duration_min'])
print(result['exercises'][0]['nf_calories'])





