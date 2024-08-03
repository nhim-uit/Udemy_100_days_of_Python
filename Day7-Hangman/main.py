# Udemy: Master Python by building 100 projects in 100 days
# Aug 03, 2024
# Day 7 - Hangman

import random as rd
from art import logo, stages
from words import word_list

print(logo)

chosen_word = rd.choice(word_list)
end_of_game = False
lives = 6

# Testing chosen word
print(f'The solution is {chosen_word}')

# Create blanks
display = ['-' for _ in chosen_word]

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    # Let user know if they've entered a guessed letter
    if guess in display:
        print(f"You've already guessed {guess}.")

    # Check guessed letter
    for pos in range(len(chosen_word)):
        if chosen_word[pos] == guess:
            display[pos] = guess

    # Check if user is wrong:
    if guess not in chosen_word:
        print(f"You guessed {guess} which is not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print('You lose.')

    # Join all the elements in the list and convert into a String
    print(f'{"".join(display)}')

    # User is right
    if '-' not in display:
        end_of_game = True
        print('You win.')

    print(stages[lives])