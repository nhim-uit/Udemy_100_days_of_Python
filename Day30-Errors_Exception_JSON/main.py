# Udemy: Master Python by building 100 projects in 100 days
# Oct 12, 2024
# Day 30 - Errors, exceptions and JSON

# FileNotFound
# with open('a_file.txt') as file:
#     file.read()

# KeyError: list index out of range
# a_dict = {'key': 'value'}
# val = a_dict['non_existent_key']

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# try:
#     Something that might cause an exception
# except:
#     Do this if there was an exception
# else:
#     Do this if there were no exceptions
# finally:
#     Do this no matter what happens

# FileNotFound
# try:
#     file = open('a_file.txt')
#     a_dict = {'key': 'value'}
#     print(a_dict['key'])
# # except:  # using bare 'except' will ignore all errors
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('Something...')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:  # will run no matter what happens
    # file.close()
    # print('File was closed.')

    # raise own exceptions:
    # raise TypeError('This is an error that I made up.')

# raise ValueError
height = float(input('Height: '))   # in meters
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not over 3 meters.')

bmi = weight / (height ** 2)
print(bmi)
