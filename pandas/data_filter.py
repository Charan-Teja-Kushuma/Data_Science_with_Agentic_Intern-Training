"""
head()
tail()
columns()
shape()
info()
"""

import pandas as pd


df = pd.read_csv("student.csv")

# print(df)
# print(df.head())
# print(df.tail())
# print(df.columns)
# print(df.shape)
# print(df.info())
Marks = df[df["Maths"] > 80]
print(Marks)