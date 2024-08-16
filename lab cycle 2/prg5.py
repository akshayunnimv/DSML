print("SJC22MCA-2009 : AKSHAY UNNI MV")
print("Batch : MCA 2023-25")
import numpy as np
even_numbers = np.arange(2, 31, 2)
alternate_elements = even_numbers[::2]
print("Original array:", even_numbers)
print("Elements from index 2 to 8 with step 2:", even_numbers[2:9:2])
print("Last 3 elements of the array using negative index:",even_numbers[-3:])
print("Alternate elements of the array:", alternate_elements)
print("Last 3 alternate elements:", alternate_elements[-3:])