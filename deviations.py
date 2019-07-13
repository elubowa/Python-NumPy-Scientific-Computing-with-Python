__author__ = 'lulu'

# ways to use deviations with Numpy.
import numpy as np

A =  np.array([[1,2],[3,4]])
print('A matrix')
print (A)
print('Standard deviation = ',np.std(A))
print('standard deviation of rows =', np.std(A, axis=0))
print('standard deviation of columns =', np.std(A, axis=1))