"""
Sales with products analysis


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('sales.csv')

# print(df)
"""
BarPlot 
"""
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

sns.barplot(
    data=product_sales,
    x="Product",
    y="Sales"
)

plt.title("Product wise Sales")
plt.show()

"""
Sales Distribution
"""
sns.histplot(data=df, x="Sales")
plt.title("Sales Distribution")
plt.show()

"""
Product Frequency

"""
sns.countplot(data=df, x="Product")
plt.title("Product Frquency")
plt.show()

"""
Outlier Detection
"""
sns.boxenplot(data=df, y="Sales")
plt.title("Sales Outlier")
plt.show()


"""
Correlation Heatmap
"""

#first adding another numeric column

df["Profit"] = df["sales"]=0.20

correlation = df[["Sales", "Profit"]].corr()

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Sales VS Profit correlation")
plt.show()