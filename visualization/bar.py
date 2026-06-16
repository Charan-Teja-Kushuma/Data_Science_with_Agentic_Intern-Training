"""
Bar aCharts

"""

import matplotlib.pyplot as plt

products = ['TVS', 'Ola', 'Ather', 'local']
sales = [48, 12, 20, 20]

plt.bar(products, sales)

plt.title("products sales presentation")

plt.show()