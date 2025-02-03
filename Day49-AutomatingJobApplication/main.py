# Udemy: Master Python by building 100 projects in 100 days
# Feb 03, 2025
# Day 49 - Auto Job Application on Linkedin
# https://www.selenium.dev/documentation/webdriver/elements/locators

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = 'my email'
ACCOUNT_PASSWORD = 'my password'
LINK = 'LINKEDIN link'
PHONE = 'my phone number'

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(LINK)

# Reject Cookies button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email = driver.find_element(by=By.ID, value='username')
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(by=By.ID, value='password')
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

# Locate the apply button
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

# Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
