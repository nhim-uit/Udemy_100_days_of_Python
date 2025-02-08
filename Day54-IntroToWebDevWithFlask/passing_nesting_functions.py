def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calc(func, a, b):
    return func(a, b)


print(calc(add, 2, 3))


# Functions can be nested in other functions
def outer_function():
    print('I\'m outer')

    def nested_function():
        print('I\'m inner')

    nested_function()


# outer_function()


# Function can be returned from other functions
def outer_function2():
    print('I\'m outer')

    def nested_function2():
        print('I\'m inner')

    return nested_function2()

inner_function2 = outer_function2()
inner_function2()