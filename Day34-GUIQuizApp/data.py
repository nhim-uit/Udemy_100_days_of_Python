import requests

params = {
    'amount': 10,
    'category': 18,
    'type': 'boolean',
}

response = requests.get(url='https://opentdb.com/api.php', params=params)
response.raise_for_status()

data = response.json()


# def create_data():
#     data_lst = []
#
#     for q in data['results']:
#         data_lst.append({['question']: q['correct_answer']})
#
#     return data_lst
