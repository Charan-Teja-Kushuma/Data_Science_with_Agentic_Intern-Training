"""
Analyze monthly products sales
1.which product sold the most
2.what is total revenue
3.what is averagae revenue 
4.which month highest sales
5.visualize sales trends

NumPy
array()

python inbuilt
sum()
mean()
max()
min()


Pandas
read_csv()
groupby()
head()
columns
info()


Matplotlib
plot()
bar()
hist()
title()
xlabel()
ylabel()

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")


"""
dataset analysis
"""
print(df.head())
print(df.info())

print("Total Records:", len(df))

print(df.columns)

"""
Numerical Dataset Analysis
"""

sales_array = np.array(df["Sales"])

print("Total Sales:", sales_array.sum())

print("Average Sales:", sales_array.mean())

print("Highest Sales:", sales_array.max())

print("Lowest sales:", sales_array.min())


"""
Product-wise Analysis ( GroupBy)

"""
products_sales = df.groupby(
    "Product"
)["Sales"].sum()

print("Sum of Products wise Sales:",products_sales)


print("Best selling item:", products_sales.idxmax())



"""
Monthly Analysis 
"""

monthly_sales = df.groupby(
    "Month"
)["Sales"].sum()

print("Sum of Monthly Sales: ", monthly_sales)

print("Highest Revenue of Month:", monthly_sales.idxmax())

"""
monthly sales trends

"""

plt.figure(figsize=(8,5))


plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.grid(True)

plt.show()


"""
Product Comparison Chart
"""

plt.figure(figsize=(8,5))


plt.bar(
    products_sales.index,
    products_sales.values
)
plt.title("Product wie Sales Trend")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()


"""
Sales distribution Histogram
"""


plt.figure(figsize=(8,5))


plt.hist(df["Sales"])

plt.title("Sales Distribution")

plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()






