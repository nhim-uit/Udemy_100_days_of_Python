# Udemy: Master Python by building 100 projects in 100 days
# Nov 04-05, 2024
# Day 35 - Rain Alert
# Using API Keys to Authenticate and get the weather from OpenWeatherMap

import requests
from send_sms import *

load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

weather_params = {
    'id': '1566083',
    'appid': api_key,
    'units': 'metric',  # Celsius
    'cnt': 4,  # 12 hours, 3-hour interval
}

# load data
response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()


# check rain
def check_rain():
    """
    print 'Bring an Umbrella' if the weather will rain (id < 700)
    :return: void
    """
    for i in range(4):
        rain_code = weather_data['list'][i]['weather'][0]['id']

        if rain_code < 700:
            # print('Bring an Umbrella')
            message = client.messages.create(
                body="It's going to rain today. Bring an Umbrella :)) ",
                from_=os.getenv('TWILIO_NUMBER'),
                to=os.getenv('MY_VIRTUAL_PHONE_NUMBER'),
            )

            print(message.status)
            return
        else:
            print(f'No rain: {rain_code}')


# call function
check_rain()
