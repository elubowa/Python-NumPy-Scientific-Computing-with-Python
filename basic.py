__author__ = 'lulu'

# Ways to work around with Numpy, using random numbers, square roots and creating matrix
import numpy as np

x=np.random.random()
print ('Randon number:',x)

x_square_root= np.sqrt(x)
print('Number sqaure root:',x_square_root)
print('x^sqrt(x)', np.power(x,x_square_root))

matrix = np.random.random(3)
matrix= np.append(matrix, np.random.random(2))

print('New matrix:',matrix)
print ('Sine of matrix:',np.sin(matrix))