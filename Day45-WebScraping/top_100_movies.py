# Udemy: Master Python by building 100 projects in 100 days
# Dec 12, 2024
# Day 45 - Web Scraping with Beautiful Soup
# Crawl data from live website
# Top 100 movies to watch of all time
# Created by me

from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://web.archive.org/web/20200518073855/'
                        'https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
titles = [title.getText() for title in titles]
sorted_titles = titles[::-1]

with open('titles.txt', 'w', encoding='utf-8') as file:
    for title in sorted_titles:
        file.write(title + '\n')
