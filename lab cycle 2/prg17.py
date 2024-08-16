print("SJC23MCA-2009 : AKSHAY UNNI M V")
print("Batch : MCA 2023-25")
import numpy as np
A = np.array([[5, 27, 32], [14, 53, 62], [67, 88, 19]])
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt
print('Original Matrix A :\n',A )
print('\nSingular Values :\n',S)
print('\nReconstructed Matrix A_hat\n:',A_hat)
