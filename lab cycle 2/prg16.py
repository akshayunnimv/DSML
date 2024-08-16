print("SJC23MCA-2009 : AKSHAY UNNI M V")
print("Batch : MCA 2023-25")
import numpy as np
A = np.array([[2, 1,-2],[3,0,1],[1,1,-1]])
B= np.array([-3,5,-2])
X = np.linalg.solve(A,B)
print("Matrix A:\n",A)
print("Vector b:\n",B)
print("Solution for X:\n",X)
