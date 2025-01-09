# Udemy: Master Python by building 100 projects in 100 days
# Dec 27, 2024
# Day 48 - Selenium Webdriver browser

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')

# driver.close() # quit a single tab
# driver.quit()  # quit the entire Chrome - multiple tabs

# try:
#     price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
#     price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
#     print(f'The price is {price_dollar.text}.{price_cents.text}')
#
#     driver.close()
# except Exception as e:
#     print(f'error {e}')

# search bar for
driver.get('https://www.python.org')

try:
    # By.NAME
    search_bar = driver.find_element(By.NAME, value='q')
    print(search_bar.get_attribute('placeholder'))

    # By.ID
    button = driver.find_element(By.ID, value='submit')
    print(button.size)

    # By.CSS_SELECTOR
    documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
    print(documentation_link.text)

    # find element by XPATH
    bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    print(bug_link.text)
except Exception as e:
    print(e)

driver.close()
