# Udemy: Master Python by building 100 projects in 100 days
# Nov 18, 2024
# Day 37 - Habit Tracking Project

import requests
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('PIXELA_USERNAME')
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = 'graph1'

# Create a user
pixela_endpoint = 'https://pixe.la/v1/users'    # Create a user

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Swimming Graph',
    'unit': 'calories',
    'type': 'int',
    'color': 'sora',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_graph.text)

# Add a pixel
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_config = {
    'date': '20241112',
    'quantity': '520',
}

response_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response_pixel.text)
