import numpy as np

# Define the matrix
M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

def swap_rows(M, a, b):
    # Sanity checks
    if not isinstance(M, np.ndarray):
        raise TypeError("M must be a NumPy array")
    if len(M.shape) != 2:
        raise ValueError("M must be a 2-dimensional array")
    if a < 0 or a >= M.shape[0] or b < 0 or b >= M.shape[0]:
        raise IndexError("Row indices are out of bounds")
    
    # Swapping rows
    M[[a, b], :] = M[[b, a], :]
    return M

def swap_cols(M, a, b):
    # Sanity checks
    if not isinstance(M, np.ndarray):
        raise TypeError("M must be a NumPy array")
    if len(M.shape) != 2:
        raise ValueError("M must be a 2-dimensional array")
    if a < 0 or a >= M.shape[1] or b < 0 or b >= M.shape[1]:
        raise IndexError("Column indices are out of bounds")
    
    # Swapping columns
    M[:, [a, b]] = M[:, [b, a]]
    return M

# Print the original matrix
print("Original matrix:")
print(M)

# Swap columns 0 and 2
print("\nMatrix after swapping columns 0 and 2:")
print(swap_cols(M.copy(), 0, 2))

# Swap rows 0 and 1
print("\nMatrix after swapping rows 0 and 1:")
print(swap_rows(M.copy(), 0, 1))
