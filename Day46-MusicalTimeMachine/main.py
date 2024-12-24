# Udemy: Master Python by building 100 projects in 100 days
# Dec 24, 2024
# Day 46 - Create a Spotify Playlist using the Musical Time Machine

import requests
from bs4 import BeautifulSoup


def get_100_songs(date_):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
                            "Gecko/20100101 Firefox/131.0"}
    url = f'https://www.billboard.com/charts/hot-100/{date_}/'
    response = requests.get(url=url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')
    heading = soup.select('li ul li h3')

    titles = [head.getText().strip() for head in heading]
    # print(titles)

    return titles


if __name__ == '__main__':
    date = input('Which year do you want to travel to? '
             'Type the date in this format YYYY-MM-DD: ')
    print(get_100_songs(date))
