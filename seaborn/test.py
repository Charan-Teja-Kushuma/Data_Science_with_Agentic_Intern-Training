"""
Seaborn : Advanced Data Visualization 

--> Better looking Charts
--> Statistical Visualization
--> Heatmaps
--> Boxplot
--> Correlation Analysis

"""

import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("sales.csv")



products_sales = df.groupby(
    "Product"
)["Sales"].sum()

plt.figure(figsize=(8,5))


plt.bar(
    products_sales.index,
    products_sales.values
)
plt.title("Product wie Sales Trend")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()

