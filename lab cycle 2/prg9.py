print("SJC23MCA-2009 : AKSHAY UNNI M V")
print("Batch : MCA 2023-25")
import numpy as np;
arr_id = np.array([1, 2, 3, 4, 5])
diagonal_matrix = np.diag(arr_id)
print("1D Array:\n",arr_id)
print("\nDiagonal Matrix:\n",diagonal_matrix)
arr_2d_square = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
diagonal_elements = np.diag(arr_2d_square)
print("\n2D Square Matrix:\n",arr_2d_square)
print("\nDiagonal Elements:\n",diagonal_elements)
arr_2d_non_square = np.array([[1, 2, 3],[4, 5, 6]])
diagonal_elements_non_square = np.diag(arr_2d_non_square)
print("\n2D Non-Square Matrix:\n",arr_2d_non_square)
print("\nDiagonal Elements (Non-Square):,\n",diagonal_elements_non_square)
