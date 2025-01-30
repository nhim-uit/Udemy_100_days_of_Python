# Udemy: Master Python by building 100 projects in 100 days
# Jan 09, 2025
# Cookie Clicker Automated Game Playing Bot
import re
from threading import Thread

SECONDS = 5
MINUTES = 1
SECOND_PER_MINUTE = 60

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')

stores = driver.find_elements(By.CSS_SELECTOR, value='.grayed')


end_time = time.time() + MINUTES * SECOND_PER_MINUTE


def func1():
    while time.time() < end_time:
        cookie.click()

def func():

    store_ids = ['buyCursor', 'buyGrandma', 'buyFactory',
                 'buyMine', 'buyShipment', 'buyAlchemy lab',
                 'buyPortal', 'buyTime machine', 'buyElder Pledge']
    available_element = {}

    for store_id in store_ids:
        element = driver.find_element(By.ID, value=store_id)
        class_attribute = element.get_attribute('class')
        if 'grayed' not in class_attribute:
            available_element[element.get_attribute('id')] = int(re.search(r'\d+', element.text).group())
            # available_element[int(re.search(r'\d+', element.text).group())] = element.get_attribute('id')

    money = int(driver.find_element(By.ID, value='money').text)
    sorted_available_element_keys = sorted(available_element.values(), reverse=True)



    try:
        # k = sorted_available_element_keys[0]
        first_key, first_value = next(iter(available_element.items()))
        i = store_ids.index(first_key)
        k = first_key
        for key in available_element:
            if store_ids.index(key) > i:
                k = key
                i = store_ids.index(key)
    except:
        print('noneeeeeeeee')

    while money >= available_element.get(k):
        print(f'k = {k}')
        el = driver.find_element(By.ID, value=k)
        el.click()
        # print(el)

        # sorted_available_element_keys.remove(k)
        # try:
        #     k = sorted_available_element_keys[0]
        # except:
        #     print('none')
        print(f'money = {money}')
        # print(sorted_available_element_keys)
        print(available_element)

        for store_id in store_ids:
            element = driver.find_element(By.ID, value=store_id)
            class_attribute = element.get_attribute('class')
            if 'grayed' not in class_attribute:
                # available_element[element.get_attribute('id')] = int(re.search(r'\d+', element.text).group())
                try:
                    # available_element[int(re.search(r'\d+', element.text).group())] = element.get_attribute('id')
                    available_element[element.get_attribute('id')] = int(re.search(r'\d+', element.text).group())
                except:
                    print('no id')
        print('---', available_element)

        sorted_available_element_keys = sorted(available_element.keys(), reverse=True)

        money = int(driver.find_element(By.ID, value='money').text)

        try:
            # k = sorted_available_element_keys[0]
            first_key, first_value = next(iter(available_element.items()))
            i = store_ids.index(first_key)
            k = first_key
            for key in available_element:
                if store_ids.index(key) > i:
                    k = key
                    i = store_ids.index(key)
        except:
            print('noneeeeeeeee2')


def func2():
    while time.time() < end_time:
        time.sleep(5)
        func()


task1 = Thread(target=func1)
task2 = Thread(target=func2)

# while True:
task1.start()
task2.start()

# task1.join()
# task2.join()
