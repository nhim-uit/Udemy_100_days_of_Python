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
        for name in file.readlines():
            name = name.strip()

            with open('./Input/Letters/starting_letter.txt', 'r') as letter:
                lines = letter.readlines()
                paragraph = ''.join(lines).split('\n')

                with open(f'./Output/letter_for_{name}', 'w') as output:
                    for line in lines:
                        if '[name]' in line:
                            line = line.replace('[name]', name)
                        output.write(line)
