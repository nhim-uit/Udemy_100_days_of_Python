# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# Cookie Clicker Automated Game Playing Bot

from threading import Thread
from functions import *
from CONSTANTS import *

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')
stores = driver.find_elements(By.CSS_SELECTOR, value='.grayed')

end_time = time.time() + MINUTES * SECOND_PER_MINUTE

task1 = Thread(target=click_cookie, args=(cookie, end_time))
task2 = Thread(target=run, args=(driver, end_time))

task1.start()
task2.start()


