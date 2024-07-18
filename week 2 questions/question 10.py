import matplotlib.pyplot as plt
import numpy as np

# generate a basic sample point array on x-axis
x = np.linspace(1, 3, 400)

# Create a piecewise linear function with different slopes
y = np.piecewise(x, [x < 2, x >= 2], [lambda x: 2*x, lambda x: -3*x + 10])

plt.plot(x, y, color = 'b', linewidth = 3)

# Add a title and labels
plt.title('Sample Graph!')
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(1, 4)
plt.xlim(1, 3)
plt.yticks(np.arange(1, 4.5, 0.5))
plt.xticks(np.arange(1, 3.5, 0.5))

plt.grid(True)

plt.show()