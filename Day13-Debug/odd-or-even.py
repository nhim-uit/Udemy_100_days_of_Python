def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."


if __name__ == '__main__':
    print(odd_or_even(12))
    print(odd_or_even(13))