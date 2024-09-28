# Udemy: Master Python by building 100 projects in 100 days
# Sep 27, 2024
# Day 25 - Squirrel Data Analysis
import pandas

if __name__ == '__main__':
    file_name = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
    data = pandas.read_csv(file_name)
    # print(data['Primary Fur Color'])
    gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
    black_count = len(data[data['Primary Fur Color'] == 'Black'])
    red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

    data_dict = {
        'Fur Color': ['Gray',
                      'Cinnamon',
                      'Black'],
        'Count': [gray_count,
                  red_count,
                  black_count]
    }

    df = pandas.DataFrame(data_dict)
    df.to_csv('squirrel_count.csv')
