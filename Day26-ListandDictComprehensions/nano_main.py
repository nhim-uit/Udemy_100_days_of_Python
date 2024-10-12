# Udemy: Master Python by building 100 projects in 100 days
# Oct 1st, 2024
# Day 26 - Nano Phonetic Alphabet Project
# Created by me

import pandas
from generate_phonetic import generate_phonetic

# load data
data = pandas.read_csv('nato_phonetic_alphabet.csv')
df = pandas.DataFrame(data)

generate_phonetic(df)


