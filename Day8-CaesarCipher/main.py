# Udemy: Master Python by building 100 projects in 100 days
# Aug 03, 2024
# Day 8 - Caesar Cipher
def caesar(plain_text, shift_amount, direction):
    if direction == 'decode':
        shift_amount *= -1

    res = ''

    for ch in plain_text:
        n = ord(ch)

        if 65 <= n <= 90:  # A-Z
            n = (n + shift_amount - 65) % 26 + 65
        elif 97 <= n <= 122:  # a-z
            n = (n + shift_amount - 97) % 26 + 97
        elif 48 <= n <= 57:  # 0-9
            n = (n + shift_amount - 48) % 10 + 48
        # else:  # Other characters stay the same
        #    n = n

        res += chr(n)

    print(f'The {direction} text is {res}.\n')


end = False

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        caesar(plain_text=text, shift_amount=shift, direction='encode')
    else:
        caesar(plain_text=text, shift_amount=shift, direction='decode')

    restart = input('Type \'yes\' if you want to go again. Otherwise type \'no\':')

    if restart == 'no':
        end = True
        print('Goodbye')

