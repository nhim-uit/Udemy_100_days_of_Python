# Udemy: Master Python by building 100 projects in 100 days
# Feb 07, 2025
# Day 53 - Capstone Project: Data Entry Job Automation
# Created by me (Alex Mai)
import re

from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Auto fill in google form for address, price and link
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)



for i in range(len(addresses)):
    driver.get('https://forms.gle/t37jcURPRFmpxEH39')

    wait = WebDriverWait(driver, 10)

    input_address = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    input_price = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    input_link = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    input_address.send_keys(addresses[i])
    input_price.send_keys(prices[i])
    input_link.send_keys(links[i])

    button = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')))
    button.click()

driver.close()
