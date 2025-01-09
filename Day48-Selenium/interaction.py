# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# interaction

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# Hone in on anchor tag using CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
all_portals.click()

# Find the 'Search' <input> by Name
search = driver.find_element(By.NAME, value='search')

search.send_keys('Python', Keys.ENTER)
