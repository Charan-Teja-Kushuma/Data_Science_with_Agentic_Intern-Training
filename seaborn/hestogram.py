import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

sns.histplot(
    data=df,
    x="Product"
)

plt.title('Seaborn Histogram')

plt.show()

