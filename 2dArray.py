"""
Numpy Array Advanced Topics 
1.2D Array
2.Array slicing
3.Reshape
4.Random data generation
5.Filtering Array 

slice syntax = array[start:stop]


"""


import numpy as np


# slice syntax = array[start:stop] # 0, 1 
data = np.array([
    # Index :  Values 
    Row 0       [1, 2, 3, 4, 5, 3, 5, 6, 7, 8],  
    Row 1       [6, 7, 8, 9, 10, 3, 5, 6, 7, 8]
])
# array([row_start:row_stop, col_start:col_stop])  #1,2
#columns iindex :0,1,2,3,4,5,6,7,8,9
# index values 
print("2d array: ", data[0:2, 1:3])