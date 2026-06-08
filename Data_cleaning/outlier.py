"""
Outliers: 

"""

import pandas as pd
import numpy as np

marks = [85, 90, 78, 92, 88, 95, 100, 150]

df = pd.DataFrame({"Marks": marks})

print(df)

X = df[df["Marks"] < 100]
print(X)