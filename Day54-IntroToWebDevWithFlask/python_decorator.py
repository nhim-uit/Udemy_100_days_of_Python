# Python Decorator Function
import time


def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        func()
        func()

    return wrapper_function


@delay_decorator
def say_hello():
    print('hello')


def say_bye():
    print('bye')


def say_greeting():
    print('How are you?')


say_bye()    # run immediately
say_hello()  # wait 2s and run
