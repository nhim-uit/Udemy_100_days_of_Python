# Udemy: Master Python by building 100 projects in 100 days
# Feb 03, 2025
# Day 49 - Auto Job Application on Linkedin
# https://www.selenium.dev/documentation/webdriver/elements/locators

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)