import numpy as np
from numpy.linalg import eig


A = np.array([
    [3,2],
    [4,1],

])


print("A = \n",A)
w,v=eig(A)
print('E-value:', w)
print('E-vector: \n', v)


