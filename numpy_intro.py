# import numpy

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# access

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

# slice

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# to the end (slice)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# from the beginning (slice)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# join

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# split

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# sort

import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


# PRACTICE— create a NumPy array of 5 numbers, find mean, sum, max

import numpy as np

# Creating NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)

# Finding sum
print("Sum:", np.sum(numbers))

# Finding mean
print("Mean:", np.mean(numbers))

# Finding maximum value
print("Maximum:", np.max(numbers)) 