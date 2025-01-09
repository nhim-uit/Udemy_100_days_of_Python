# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# automatically sign up

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://secure-retreat-92358.herokuapp.com')

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys('Alex')
last_name.send_keys('M')
email.send_keys('alex.m@gmail.com', Keys.ENTER)
