import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

sns.pairplot(
    df
)

plt.show()

