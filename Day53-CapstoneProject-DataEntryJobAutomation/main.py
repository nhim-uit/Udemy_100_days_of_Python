# Udemy: Master Python by building 100 projects in 100 days
# Feb 07, 2025
# Day 53 - Capstone Project: Data Entry Job Automation
# Created by me (Alex Mai)
import re

from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# crawl data for address, price and link from Zillow
response = requests.get('https://appbrewery.github.io/Zillow-Clone/')

soup = BeautifulSoup(response.text, 'html.parser')

addresses = [tag.select_one(selector='address').getText().strip().replace(',', '').replace(' | ', '')
             for tag in soup.select('.StyledPropertyCardDataWrapper')]
prices = [re.sub(r'[^\d,$]', '',
                 tag.find(name='span', class_='PropertyCardWrapper__StyledPriceLine').getText().replace('+/mo', ''))
          for tag in soup.select('.PropertyCardWrapper')]
links = [tag.get('href')
         for tag in soup.select('.StyledPropertyCardDataArea-anchor')]




