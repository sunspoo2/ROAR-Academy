import numpy as np

def set_array(L, rows, cols):
    if not isinstance(L, list):
        raise TypeError("L must be a list")
    if len(L) != rows * cols:
        raise ValueError("The number of elements in L must be equal to rows * cols")
    
    # Create the numpy array in row-major order
    M = np.array(L).reshape((rows, cols))
    return M

L = [1, 2, 3, 4, 5, 6]
rows = 2
cols = 3

# Create the NumPy array
M = set_array(L, rows, cols)
print(M)