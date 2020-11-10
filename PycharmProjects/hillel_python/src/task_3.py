import os
import pandas as pd


file_name = 'UCI_Credit_Card.csv'

# folder_name = 'datasets'
# file_path = os.path.join(folder_name, file_name)
# print(file_path)

df = pd.read_csv(file_name)

# print(df.head(10))
# print(df['PAY_AMT5'])
# print('Sum for PAY_AMT5:')
# print(df['PAY_AMT5'].sum())
# print(df2.head(10))
# # df2.to_csv('edu_3.csv')

df2 = df[df['EDUCATION'] == 3]
print(df2.shape)