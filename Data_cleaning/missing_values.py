"""
1.missing values
2.duplicate values or records
3.incorrect data  = Data Type Cleaning
4.outliers
5.formatting issues
6.inconsistent values 


data cleaning workflow

Raw Data
    ↓
Missing Values
    ↓
Duplicates
    ↓
Outliers
    ↓
Incorrect Formats
    ↓
Clean Dataset


"""

# 1.Missing Values:
import pandas as pd
import numpy as np

data ={ 
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, np.nan, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", np.nan, "Phoenix"],
    "Salary": [50000, 60000, 70000, 80000, np.nan],
}


df = pd.DataFrame(data)

print(df)


X = df.isnull()
print(X)

Z = X.sum()
print(Z)


df["Age"].fillna(0, inplace=True)
df["City"].fillna("Unknown", inplace=True)
df["Salary"].fillna(0, inplace=True)



print(df)

