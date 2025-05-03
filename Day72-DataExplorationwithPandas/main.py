# Udemy: Master Python by building 100 projects in 100 days
# Apr 26, 2025
# Day 73 - College major vs. Salary

import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna())
# print(df.tail())

clean_df = df.dropna()
# print(clean_df)
# print(clean_df['Starting Median Salary'].max())
# print(clean_df['Starting Median Salary'].idxmax())
# print(clean_df['Undergraduate Major'].loc[43])
print(clean_df['Undergraduate Major'][43])
print(clean_df.loc[43])
clean_df['Mid-Career 10th Percentile Salary'].max()
clean_df['Mid-Career 10th Percentile Salary'].max()

clean_df['Starting Median Salary'].idxmin()
clean_df['Undergraduate Major'].loc[49]

clean_df['Mid-Career Median Salary'].idxmax()
clean_df['Undergraduate Major'].loc[8]

clean_df['Mid-Career Median Salary'].idxmin()
clean_df['Undergraduate Major'].loc[18]

clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

res = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False).head()

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

clean_df.groupby('Group').count()
clean_df.groupby('Group')