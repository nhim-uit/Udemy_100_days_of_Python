# Udemy: Master Python by building 100 projects in 100 days
# Sep 26, 2024
# Day 24 - Files, directories and paths
# Mail Merge Challenge

# with open('my_file.txt', 'r') as file:
#     print(file.read())  # read contents of the file
#
# with open('my_file.txt', 'w') as file:      # 'w' as rewrite the file
#     file.write('New text')
#
# with open('my_file_1.txt', 'w') as file:    # 'w' as writing the new file
#     file.write('New text')
#
# with open('my_file.txt', 'a') as file:      # 'a' as append new contents to the file
#     file.write('\nNew text 1')

if __name__ == '__main__':
    with open('./Input/Names/invited_names.txt', 'r') as file:
        names = file.readlines()

    with open('./Input/Letters/starting_letter.txt', 'r') as letter:
        letter_content = letter.read()

    for name in names:
        new_letter = letter_content.replace('[name]', name.strip())

        with open(f'./Output/letter_for_{name.strip()}.txt', 'w') as output:
            output.write(new_letter)
