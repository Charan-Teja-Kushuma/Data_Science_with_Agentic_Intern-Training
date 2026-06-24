"""
Netflix Data Analysis

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mymoviedb.csv", lineterminator='\n')

print(df)