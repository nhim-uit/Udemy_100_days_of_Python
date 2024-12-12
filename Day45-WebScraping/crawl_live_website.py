# Udemy: Master Python by building 100 projects in 100 days
# Dec 12, 2024
# Day 45 - Web Scraping with Beautiful Soup
# Crawl data from live website
# Created by me

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

articles_texts = [tag.select_one(selector='a').getText() for tag in soup.select('.titleline')]
articles_links = [tag.select_one(selector='a').get('href') for tag in soup.select('.titleline')]
articles_upvote = [s.getText() for s in soup.find_all(name='span', class_='score')]
