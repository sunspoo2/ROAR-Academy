import numpy as np
z = 2  # Keep z as a 1D array for element-wise multiplication
a = np.array([
[6, -9, 1],
[4, 24, 8]
])

b = np.array([
[1, 0],
[0, 1]
])
c = np.array([
[6, -9, 1],
[4, 24, 8]
])

d = np.array([
[4, 3],
[3, 2]
])

e = np.array([
[-2, 3],
[3, -4]
 ])

print(np.dot(z, a))
print(np.dot(b, c))
print(np.dot(d, e))
