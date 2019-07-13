__author__ = 'lulu'

from numpy import  linalg
import numpy as np

A = np.diag((1,2,3))
print ('A matrix: ')
print (A)

eigenvalues,_ = linalg.eig(A)
print('Eigenvalues: ')
print(eigenvalues)