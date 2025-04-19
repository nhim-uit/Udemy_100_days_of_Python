# Udemy: 100 days of Python
# April 15th, 2025
# Text to Morse Code Converter

alphabet_to_morse_code = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    '0': '_____',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
}


def translate(s, d):
    temp = s.split(' ')
    res = ''

    for i in temp:
        res += d[i] + ' '

    return res


def create_morse_code_dict(d):
    res = {}

    for i in d.keys():
        res[d[i]] = i

    return res


if __name__ == '__main__':
    print(translate('m o r s e c o d e', alphabet_to_morse_code))
    print(translate('_._. ___ _.. .', create_morse_code_dict(alphabet_to_morse_code)))
