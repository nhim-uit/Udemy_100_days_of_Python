# Udemy: Master Python by building 100 projects in 100 days
# May 03, 2025
# Day 73 - Data Visualization with Matplotlib

import pandas as pd
from sympy.printing.pretty.pretty_symbology import line_width

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# print(df.head())
# print(df.tail())

# number of columns
# print(df.shape) # 1992 rows, 3 columns

# count the number of entries in each column
# print(df.count())

# use group by to see number of entries and posts by programming language
# print(df.groupby('TAG').sum())

# use count() in each column, we can see how many months of entries exist per progamming language
# print(df.groupby('TAG').count())

# DATA CLEANING
df['DATE'][1]
df.DATE[1]

# print(type(df['DATE'][1]))

# print(pd.to_datetime(df.DATE[1]))
# print(type(pd.to_datetime(df.DATE[1])))

# convert DATE from str to datetime
df.DATE = pd.to_datetime(df.DATE)
# print(df.head())

# df.dropna()
pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# print(pivoted_df.head())

# substitute the number 0 for each NaN value
pivoted_df.fillna(0, inplace=True)
# print(pivoted_df.head())

# check if there are any NaN values left in df
# print(pivoted_df.isna().values.any())

# import
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# for c in pivoted_df.columns:
#     plt.plot(pivoted_df.index, pivoted_df[c],
#              linewidth=3, label=pivoted_df[c].name)

plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.legend(fontsize=16)

# Show the plot
# plt.show()

# Smoothing out the data
roll_df = pivoted_df.rolling(window=12).mean()

for c in roll_df.columns:
    plt.plot(roll_df.index, roll_df[c],
             linewidth=3, label=roll_df[c].name)

plt.legend(fontsize=16)
plt.show()

