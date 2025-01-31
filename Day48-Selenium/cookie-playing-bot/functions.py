import time
import re
from CONSTANTS import STORE_IDS, SECONDS
from selenium.webdriver.common.by import By


def click_cookie(cookie, end_time):
    while time.time() < end_time:
        cookie.click()


def fill_available_element(driver):
    available_element = {}
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


def autobuy(driver, end_time):
    available_element = fill_available_element(driver)
    money = int(driver.find_element(By.ID, value='money').text)

    if available_element:
        k = get_key_has_largest_value(available_element)
        v = available_element.get(k)

    while time.time() < end_time:
        el = driver.find_element(By.ID, value=k)

        if v:
            if money >= v:
                el.click()

        available_element = fill_available_element(driver)

        if available_element:
            k = get_key_has_largest_value(available_element)
            v = available_element.get(k)


def run(driver, end_time):
    while time.time() < end_time:
        time.sleep(SECONDS)
        autobuy(driver, end_time)
    print('==============END=============')
