import numpy as np

# Input
z = np.array([[37, 20, 12],
              [15, 32, 4],
              [5,  40, 2]
             ])
r = np.array([[435],[178],[70]])

# Method 1: Using inverse of matrix
print(np.linalg.inv(z))
X = np.linalg.inv(z).dot(r)
print(X)

# Method 2: Using solve() function
y = np.linalg.solve(z,r)
print(y)

# Concatenation
a = np.array([[37, 20, 12]])
b = np.array([[15, 32, 4]])
c = np.array([[5,  40, 2]])

u = np.concatenate((a, b, c), axis=0)
print(u)
