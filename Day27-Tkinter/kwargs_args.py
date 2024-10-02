# Udemy: Master Python by building 100 projects in 100 days
# Oct 2nd, 2024
# Day 27 - *args, **kwargs

def add(*args):
    s = 0

    # args is tuple
    for num in args:
        s += num

    return s


def calculate(n, **kwargs):
    print(kwargs)

    # kwargs is dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs['add'])
    # n += kwargs['add']
    # n *= kwargs['multiply']
    # this will return error if no key word is found

    # use this instead
    n1 = kwargs.get('add')
    n2 = kwargs.get('multiply')
    n3 = kwargs.get('divide')
    n4 = kwargs.get('subtract')

    if n1:
        n += n1

    if n2:
        n *= n2

    if n3:
        n /= n3

    if n4:
        n -= n4

    return n


if __name__ == '__main__':
    print(add(1, 2, 5, 7, 9))
    print(add(1, 2, 3))

    print(calculate(5, add=3, multiply=5))
