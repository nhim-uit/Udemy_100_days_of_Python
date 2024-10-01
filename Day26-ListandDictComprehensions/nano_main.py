# Udemy: Master Python by building 100 projects in 100 days
# Oct 1st, 2024
# Day 26 - Nano Phonetic Alphabet Project
# Created by me

import pandas

# load data
data = pandas.read_csv('nato_phonetic_alphabet.csv')
df = pandas.DataFrame(data)

# get input from user
name = input('Enter a name: ').upper()
list_ch = list(name.replace(' ', '')) # split string into characters, ignore space character

# create a list of codes matching characters in input string
result = [df.query('letter == @ch').code.to_string(index=False, header=False) for ch in list_ch]

print(result)

