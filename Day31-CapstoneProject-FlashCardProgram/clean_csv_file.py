# Oct 16, 2024
# Clean data csv file, which contains '?' in  Vietnamese word
# Created by me

import pandas

df = pandas.read_csv('data1.csv')
df_cleaned = df[~df['Vietnamese'].str.contains('\?', na=False)]
print(df_cleaned)

df_cleaned.to_csv('cleaned_file.csv', index=False, encoding='utf-8')
