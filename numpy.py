import numpy as np

# normal way 

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# numpy way
    
a = np.array[1, 2, 3, 4]
b = np.array[1, 2, 3, 4]

a * b

# numpy array

np.array([1, 2, 3, 4, 5])

np.zeros(10, dtype=int)

np.random.randint(0, 10, size=10)

np.random.normal(10, 4, (3, 4))

# attributes of numpy array

a = np.random.randint(1, 10, size=9)
a.ndim
a.shape
a.size
a.dtype

# reshaping

np.random.randint(1, 20, size=9).reshape(3, 3)

# index selection
a = np.random.randint(10, size=10)
a[0]
a[0:5] #zero to five

m = np.random.randint(1, 20, size=9).reshape(3, 3)
m[0][0]
m[0:2, 0:3]

# numpy condition

v= np.arange(0, 30, 3)
v[v < 5]

# numpy mathematics

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10_ 

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)

