"""
Pie charts

"""

import matplotlib.pyplot as plt

labels = ["Mobile", "laptops", "Tablet"]

sales = [50, 30, 20]


plt.pie(
    sales,
    labels=labels,
    autopct="%1.1f%%"
)

plt.show()
