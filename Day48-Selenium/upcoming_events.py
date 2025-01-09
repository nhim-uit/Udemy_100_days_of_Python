# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# Get a dictionary of upcoming events from python.org

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.python.org')

try:
    events_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
    events_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu a')

    events = {i: {'time': t.text, 'name': n.text} for i, (t, n) in enumerate(zip(events_times, events_names))}

    print(events)
except Exception as e:
    print(e)
finally:
    driver.close()
