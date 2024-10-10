import random
import string


def generate_random_password():
    no_letters = random.randint(8, 10)
    no_symbols = random.randint(2, 4)
    no_numbers = random.randint(2, 4)

    alphabets = list(string.ascii_lowercase)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(alphabets) for _ in range(no_letters)]
    password_list += [random.choice(symbols) for _ in range(no_symbols)]
    password_list += [str(random.randint(0, 9)) for _ in range(no_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    return password
