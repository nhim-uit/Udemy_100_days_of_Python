# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# Cookie clicker

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')

for i in range(10):
    cookie.click()
