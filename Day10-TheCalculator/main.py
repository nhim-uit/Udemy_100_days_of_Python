# Udemy: Master Python by building 100 projects in 100 days
# Aug 06, 2024
# Day 10 - The Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    end = False
    n1 = float(input('Enter first number = '))

    while not end:
        for _ in operations:
            print(_)

        symbol = input('Pick an operation: ')
        n2 = float(input('Enter second number = '))
        ans = operations[symbol](n1, n2)
        print(f'{n1} {symbol} {n2} = {ans}')

        choice = input(f"Type 'y' to continue calculating with {ans}, " 
        "type 'n' to start with a new number, " 
        "type 'end' to end the program: ")

        if choice == 'y':
            n1 = ans
        elif choice == 'n':
            calculator()
        else:
            end = True


if __name__ == '__main__':
    calculator()




