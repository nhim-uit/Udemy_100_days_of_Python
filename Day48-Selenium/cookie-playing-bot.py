# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# Cookie Clicker Automated Game Playing Bot
import re

SECONDS = 5
MINUTES = 0.125
SECOND_PER_MINUTE = 60

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')

stores = driver.find_elements(By.CSS_SELECTOR, value='.grayed')
store_info = {}

for element in stores[:-1]:
    if element is not None:
        element_text = element.text
        element_name = element.get_attribute('id')
        element_price = int(re.search(r'\d+', element_text).group())
        store_info[element_name] = element_price

