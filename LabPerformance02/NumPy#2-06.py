# NumPy#2: Create an array of 100 random values and normalize them between 0 and 1.

import numpy as np

arr = np.random.rand(100)  

arrayMin, arrayMax = arr.min(), arr.max()
norArray = (arr - arrayMin) / (arrayMax - arrayMin)

print("array:\n", arr)
print("\n normalized array:\n", norArray)
