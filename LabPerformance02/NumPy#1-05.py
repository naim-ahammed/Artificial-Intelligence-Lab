# NumPy#1: Generate a 5x5 matrix of random integers and compute row-wise sums.

import numpy as np

matrix = np.random.randint(1, 101, (5, 5))

RS = matrix.sum(axis=1)

print("matrix is:\n", matrix)
print("row wise sums:", RS)
