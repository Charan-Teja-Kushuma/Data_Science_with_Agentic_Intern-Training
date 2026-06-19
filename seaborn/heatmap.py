import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True
)

plt.show()

