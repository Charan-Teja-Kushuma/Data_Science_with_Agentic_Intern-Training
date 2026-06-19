import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

sns.barplot(
    data=df,
    x="Product",
    y="Sales"
)

plt.title('Seaborn Bar')

plt.show()

