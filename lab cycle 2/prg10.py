print("SJC23MCA-2009 : AKSHAY UNNI M V")
print("Batch : MCA 2023-25")
import numpy as np;
matrix_size = 3
matrix = np.random.randint(10,20, size=(matrix_size, matrix_size))
print("Original Matrix:\n",matrix)
if np.linalg.matrix_rank(matrix) == matrix_size:
    inverse_matrix = np.linalg.inv(matrix)
    print("\nInverse Matrix:")
    print(inverse_matrix)
else:
    print("\nThe matrix is not invertible (its rank is less than the size).")
print("\nRank of the Matrix:", np.linalg.matrix_rank(matrix))
print("\nDeterminant of the Matrix:", np.linalg.det(matrix))
print("\nMatrix as 1D Array:\n",matrix.flatten())
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues:\n",eigenvalues)
print("\nEigenvectors:\n",eigenvectors)
