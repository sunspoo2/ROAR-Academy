import numpy as np
arr = np.array([
	[0, 1, 2, 3, 4, 5],
	[10, 11, 12, 13, 14, 15],
	[20, 21, 22, 23, 24, 25],
	[30, 31, 32, 33, 34, 35],
	[40, 41, 42, 43, 44, 45],
	[50, 51, 52, 53, 54, 55]
])

pink = arr[1, 2:4]
print(pink)

green = np.concatenate((arr[2, 4:6], arr[3, 4:6])).reshape(2, 2)
print(green)

blue = arr[:, 1]  # Extracting the second column from all rows
print(blue)

orange_elements = np.array([
    arr[3, 0], arr[3, 3], arr[3, 4], 
    arr[4, 0], arr[4, 3], arr[4, 4]
])
print(orange_elements)

