# Udemy: Master Python by building 100 projects in 100 days
# Sep 26, 2024
# Day 25 - CSV and pandas

# import csv
import pandas

if __name__ == '__main__':
    # readlines
    # with open('weather_data.csv', 'r') as file:
    #     data = file.readlines()
    #     print(data)

    # csv
    # with open('weather_data.csv') as file:
    #     data = csv.reader(file)
    #     temperatures = []
    #     for row in data:
    #         # print(row)
    #         if row[1].isdigit():
    #             temperatures.append(int(row[1]))
    #
    #     print(temperatures)

    # pandas
    data = pandas.read_csv('weather_data.csv')
    # print(data['temp'])

    data_dict = data.to_dict()
    # print(data_dict)

    # calculate mean of temperatures using list
    # temp_list = data['temp'].to_list()
    # print(temp_list)
    # average = sum(temp_list) / len(temp_list)
    # print(f'{average:.2f}')

    # calculate mean of temperatures using built-in function
    print(f"{data['temp'].mean():.2f}")
    print(data['temp'].max())

    # get data in columns
    print(data['condition'])    # get a list
    # same as
    print(data.condition)       # get an object

    # 2 primary data structures of pandas: Series (1-d) and DataFrame (2-d)
    # Series is 1-d, equivalent to a list, single column
    # DataFrame is 2-d, equivalent to a table
    # pandas.pypanda.org

    # get data in row
    monday = data[data.day == 'Monday']
    print(monday)
    print(monday.condition)

    # which day has the highest temperature in a week
    print(data[data.temp == data.temp.max()])

    # convert monday temperature C into F
    print(monday.temp * 9/5 + 32)
