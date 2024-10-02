# Udemy: Master Python by building 100 projects in 100 days
# Oct 2nd, 2024
# Day 27 - *args, **kwargs

def add(*args):
    s = 0

    # args is tuple
    for num in args:
        s += num

    return s


if __name__ == '__main__':
    print(add(1, 2, 5, 7, 9))
    print(add(1, 2, 3))
