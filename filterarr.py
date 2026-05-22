import numpy as np

data = np.array([45, 78, 90, 32, 85])

X = data > 50
print(data[X])