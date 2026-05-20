""" create a 10 students marks list
Outputs:
Print all students marks
1. Total marks
2. Average marks
3. Highest marks
4. Lowest marks  """

import numpy as np

M = np.array([45, 76, 44, 88, 77, 90, 67, 80, 55, 92])


print("Student Marks: ", M)

print("Total Marks: ", np.sum(M))
print("Average Marks: ", np.mean(M))
print("Highest Marks: ", np.max(M))
print("Lowest Marks: ", np.min(M))

