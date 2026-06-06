"""
Duplicate Values  Data Handling

1.find the duplicate values
2.count the duplicate values
3.remove the duplicate values

"""

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, 40, 45, 25],
}


df = pd.DataFrame(data)
print(df)

# 1.find the duplicate values
X = df.duplicated()

print(X)

# 2.count the duplicate values
Y = df.duplicated().sum()

# Y = X.sum()
print(Y)


# 3.remove the duplicate values
Z = df.drop_duplicates()
print(Z)

