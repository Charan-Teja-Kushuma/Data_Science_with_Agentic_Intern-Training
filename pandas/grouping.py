"""
groupby function
aggregation funtion
sorting function
value count function

"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Salary": [50000, 60000, 70000, 80000, 90000],
}

df = pd.DataFrame(data)


# avg = df.groupby("City")["Salary"].mean()

# print(df)
# print(avg)
# srt = df.sort_values(by="Age", ascending=True)
# print(srt)

X = df["City"].value_counts()
print(X)




