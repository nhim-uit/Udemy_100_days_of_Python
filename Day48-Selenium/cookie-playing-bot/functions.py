import time
import re
from CONSTANTS import STORE_IDS, SECONDS
from selenium.webdriver.common.by import By


def click_cookie(cookie, end_time):
    """

    :param cookie: cookie object
    :param end_time:
    :return: void
    """
    while time.time() < end_time:
        cookie.click()


def fill_available_element(driver):
    """

    :param driver:
    :return: a list of available non-grayed elements (upgrades that can be bought)
    """
    available_element = {}
    for store_id in STORE_IDS:
        element = driver.find_element(By.ID, value=store_id)
        class_attribute = element.get_attribute('class')
        if 'grayed' not in class_attribute:
            available_element[element.get_attribute('id')] = int(re.search(r'\d+', element.text).group())
    return available_element


def get_key_has_largest_value(available_element):
    """

    :param available_element:
    :return: an upgrade element that can be bought (the highest valued element)
    """
    first_key, first_value = next(iter(available_element.items()))
    i = STORE_IDS.index(first_key)
    k = first_key

    for key in available_element:
        if STORE_IDS.index(key) > i:
            k = key
            i = STORE_IDS.index(key)

    return k


def autobuy(driver, end_time):
    """
    autobuy the element that has the highest value
    :param driver:
    :param end_time:
    :return: void
    """
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
    """
    run the autobuy function in a time frame
    :param driver:
    :param end_time:
    :return:
    """
    while time.time() < end_time:
        time.sleep(SECONDS)
        autobuy(driver, end_time)
    print('==============END=============')
