import numpy as np 
a = np.array([1,2,3,4,5])
b = np.array((5,4,3,2,1))
print(a)
print(b)
print(type(a))
print(type(b))
#data type
print(a.dtype)

                        #Dimension

import numpy as np
x = np.array([[2,3,4,5],[2,4,7,8]])
print(x.ndim)
#Access
print(x[0,1])

# 1D

import numpy as np
a = np.array([10, 20, 30, 40])
print(a.ndim)     # 1D
print(a[0])       # 10  -> First element
print(a[2])       # 30  -> Third element

# 2D

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(b.ndim)     # 2D
print(b[0, 1])    # Row 0, Column 1 -> 2
print(b[2, 2])    # Row 2, Column 2 -> 9

# 3D

c = np.array([
    [[1, 2], [3, 4],[8,9]],
    [[5, 6], [7, 8],[9,11]]
])

print(c.ndim)     # 3D
print(c[0, 1, 0]) # First "layer", row 1, column 0 -> 3
print(c[1, 0, 1]) # Second "layer", row 0, column 1 -> 6


                               # Important Functiom

#1 Array Creation
import numpy as np

np.zeros((2, 3))                     # 2x3 array filled with 0s
np.ones((3, 3))                      # 3x3 array filled with 1s
np.full((2, 2), 7)                   # 2x2 array filled with 7
np.arange(0, 10, 2)                  # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)                 # 5 numbers evenly spaced between 0 and 1
np.eye(3)                            # 3x3 Identity matrix
np.random.rand(5,2)                  # Random floats 
np.random.randint(1, 10, size=(2,2)) # Random integers

#2 Array Information
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape     # (2, 3) -> rows, columns
arr.ndim      # Number of dimensions
arr.size      # Total elements
arr.dtype     # Data type
arr.itemsize  # Bytes per element

# 3 Indexing & Slicing
arr[0, 1]      # Row 0, Col 1
arr[:, 1]      # All rows, Col 1
arr[0:2, 0:2]  # Rows 0-1, Cols 0-1
arr[-1]        # Last row

#4 Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b          # Element-wise addition
a - b          # Element-wise subtraction
a * b          # Element-wise multiplication
a / b          # Element-wise division
np.sqrt(a)     # Square root
np.exp(a)      # Exponential
np.log(a)      # Natural log

#5 Aggregate Functions
arr.sum()          # Sum of all elements
arr.mean()         # Mean value
arr.min()          # Minimum
arr.max()          # Maximum
arr.std()          # Standard deviation
arr.var()          # Variance
arr.sum(axis=0)    # Sum by column
arr.sum(axis=1)    # Sum by row

#6 Reshaping & Stacking
arr.reshape(3, 2)                # Change shape
arr.flatten()                    # Convert to 1D
np.hstack([a, b])                 # Horizontal stack
np.vstack([a, b])                 # Vertical stack

#7 Sorting & Unique
np.sort(arr)       # Sort array
np.unique(arr)     # Get unique values

#8 Boolean Filtering
arr = np.array([1, 2, 3, 4, 5])
arr[arr > 2]       # [3, 4, 5]

                                  # More indexing


i = np.arange(1, 101)  # Start at 1, stop before 101
print(i)
o = i[[0,2,3,4,5]]
print(o)

p = i[i<11]
print(p)

#############################################
array1 =np.round(10*np.random.rand(11,2))
print(array1)


                             #Linear Algebra Operations in NumPy
#Matrix Multiplication
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = np.dot(A, B)      # Method 1
result2 = A @ B            # Method 2 (Python operator)
print(result)

#Determinant
det = np.linalg.det(A)
print(det)
#Inverse of a Matrix
inv_A = np.linalg.inv(A)
print(inv_A)
#Solve Linear Equations
#2x + y = 8  
#x - y = 2
coeff = np.array([[2, 1],
                  [1, -1]])
const = np.array([8, 2])

solution = np.linalg.solve(coeff, const)
print(solution)  # [x, y]
#Eigenvalues and Eigenvectors
values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)


