# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# Get a dictionary of number of articles based on languages on Wikipedia

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.wikipedia.org')

try:
    languages = driver.find_elements(By.CSS_SELECTOR, value='.central-featured-lang strong')
    articles = driver.find_elements(By.CSS_SELECTOR, value='.central-featured-lang small')

    no_of_articles = [{'language': language.text, 'article': article.text}
                      for language, article in zip(languages, articles)]
    print(no_of_articles)
except Exception as e:
    print(e)
finally:
    driver.close()

