# Udemy: Master Python by building 100 projects in 100 days
# Feb 07, 2025
# Day 50 - Auto Tinder Bot
# Created by me (Alex Mai)

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://tinder.com/app/recs')

try:
    reject = driver.find_element(By.XPATH, value='//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button')

    for _ in range(100):
        sleep(2)
        reject.click()
except NoSuchElementException:
    sleep(2)

driver.close()
