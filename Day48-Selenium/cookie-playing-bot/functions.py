import time
import re
from CONSTANTS import STORE_IDS
from selenium.webdriver.common.by import By


def click_cookie(cookie, end_time):
    while time.time() < end_time:
        cookie.click()


def fill_available_element(available_element, driver):
    for store_id in STORE_IDS:
        element = driver.find_element(By.ID, value=store_id)
        class_attribute = element.get_attribute('class')
        if 'grayed' not in class_attribute:
            available_element[element.get_attribute('id')] = int(re.search(r'\d+', element.text).group())
    return available_element


def get_key_has_largest_value(available_element):
    first_key, first_value = next(iter(available_element.items()))
    i = STORE_IDS.index(first_key)
    k = first_key

    for key in available_element:
        if STORE_IDS.index(key) > i:
            k = key
            i = STORE_IDS.index(key)

    return k


def autobuy(driver):
    available_element = fill_available_element({}, driver)
    k = get_key_has_largest_value(available_element)
    money = int(driver.find_element(By.ID, value='money').text)

    while money >= available_element.get(k):
        print(f'k = {k}')
        el = driver.find_element(By.ID, value=k)
        el.click()

        print(f'money = {money}')
        print(available_element)

        try:
            available_element = fill_available_element(available_element, driver)
            print('---', available_element)
        except:
            print('$available element$')

        try:
            k = get_key_has_largest_value(available_element)
        except:
            print('$key largest value$')

        money = int(driver.find_element(By.ID, value='money').text)


def run(driver, end_time):
    while time.time() < end_time:
        time.sleep(5)
        autobuy(driver)
