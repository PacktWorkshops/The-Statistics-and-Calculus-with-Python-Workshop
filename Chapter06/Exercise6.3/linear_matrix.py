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

# Method 2
a =  np.dot(np.linalg.inv(z), w)

z = np.array([[3,2],[-6,6]])
print(np.linalg.det(z))
print(np.linalg.inv(z))
w = np.array([[7],[6]])

a =  np.dot(np.linalg.inv(z), w)
print(a)


37*10 + 20*0.25 + 12*5 = 435
15*10 + 32*0.25 + 4*5 =  178
5*10 + 40*0.25 + 2*5 = 70

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']
test = zip(list1, list2)
test = [list(i) for i in test]
print(test)
test = np.array(test)
print(type(test))
