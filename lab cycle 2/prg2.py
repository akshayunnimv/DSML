print("SJC23MCA-2009 : AKSHAY UNNI M V")
print("Batch : MCA 2023-25")
import numpy as np
array_2d = np.array([ [1 + 2j, 3 + 4j, 5 + 6j], [7 + 8j, 9 + 10j,
11 + 12j] ], dtype=complex)
print("2D Array:\n",array_2d)
rows, columns = array_2d.shape
print("\nNumber of Rows:", rows,"\nNumber of Columns:", columns)
dimensions = array_2d.ndim
print("\nDimensions of the Array:", dimensions)
print("\nReshaped Array (3x2):\n",array_2d.reshape(3, 2))
