"""Program for shape your file"""


import pandas as pd


def print_shape():
    """Function to print your file"""

    return print(df.shape)


your_file = input('Enter file name:')

df = pd.read_csv(your_file)

your_file = df

print_shape()
