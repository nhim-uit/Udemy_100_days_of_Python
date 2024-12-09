# Udemy: Master Python by building 100 projects in 100 days
# Dec 06, 2024
# Day 45 - Web Scraping with Beautiful Soup
# https://crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1', id='name')
print(heading)

h3_heading = soup.find(name='h3', class_='heading')
print(h3_heading)
