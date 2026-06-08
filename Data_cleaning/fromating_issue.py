"""
Formating Issues (String Cleaning)


" Rahul "
"Subbu"
"Priya "



"""


import pandas as pd
import numpy as np

data = {
    "Name": [" Rahul ", "Subbu", "Priya "],
    "City": [" New York ", "Los Angeles", " Chicago "],
}
df = pd.DataFrame(data)

# print(df)

# X = df["Name"].str.strip()
# Y = df["City"].str.strip()

# print(X)
# print(Y)

# convert to uppercase
# U = df["Name"].str.upper()
# print(U)


#conver to lower case
# L = df["City"].str.lower()
# print(L)


#convert to title case 
T = df["Name"].str.title()
print(T)
