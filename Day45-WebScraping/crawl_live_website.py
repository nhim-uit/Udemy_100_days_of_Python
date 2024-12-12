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
# print(articles_upvote)

upvote = list(filter(None, [int(s.split()[0]) if 'points' in s else None for s in articles_upvote]))
# print(upvote)

# Zip the lists into a list of dictionaries
articles = [{'text': text, 'link': link, 'upvote': up}
            for text, link, up in zip(articles_texts, articles_links, upvote)]

# Find the article with the maximum upvote
max_upvote_article = max(articles, key=lambda x: x['upvote'])

print(max_upvote_article)

# notes
# https://news.ycombinator.com/robots.txt
# to know what we can crawl from a website
# recommend not to crawl more than 1 per minute
