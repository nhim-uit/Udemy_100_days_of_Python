# Udemy: Master Python by building 100 projects in 100 days
# Nov 20, 2024
# Day 38 - Working Out Tracking Using Google Sheets

import os
import requests
from datetime import datetime
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
print(result)

# SHEETY API
SHEETY_API_KEY = os.getenv('SHEETY_API_KEY')

sheety_endpoint = f'https://api.sheety.co/{SHEETY_API_KEY}/copyOfMyWorkouts/workouts'

today = datetime.now().date().strftime('%d/%m/%Y')
current_time = datetime.now().time().strftime('%H:%M:%S')
# print(current_time)

sheety_headers = {
    'Authorization': os.getenv('SHEETY_HEADER'),
}

for exercise in result['exercises']:
    sheety_params = {
        'workout': {
            'date': today,
            'time': current_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_params)
    print(sheety_response.text)
