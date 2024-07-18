import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()

sample_count = 100
x_sample = 10 * np.random.random(sample_count) - 5
y_sample = 2 * x_sample - 1 + np.random.normal(0, 1.0, sample_count)

# plots the parameter space
ax2 = fig.add_subplot(1, 1, 1, projection='3d')

def penalty(para_a, para_b):
    global x_sample, y_sample, sample_count

    squares = (y_sample - para_a * x_sample - para_b) ** 2
    return 1 / 2 / sample_count * np.sum(squares)

a_arr, b_arr = np.meshgrid(np.arange(-2, 4, 0.1), np.arange(-2, 4, 0.1))

func_value = np.zeros(a_arr.shape)
for x in range(a_arr.shape[0]):
    for y in range(a_arr.shape[1]):
        func_value[x, y] = penalty(a_arr[x, y], b_arr[x, y])

ax2.plot_surface(a_arr, b_arr, func_value, color='red', alpha=0.8)
ax2.set_xlabel('a parameter')
ax2.set_ylabel('b parameter')
ax2.set_zlabel('f(a, b)')

# Plot the gradient descent
def grad(aa):
    grad_aa = np.zeros(2)
    update_vector = (y_sample - aa[0] * x_sample - aa[1])
    grad_aa[0] = -1 / sample_count * x_sample.dot(update_vector)
    grad_aa[1] = -1 / sample_count * np.sum(update_vector)
    return grad_aa

initial_position = np.array([-2, 2])
epsilon = 0.001

learning_rates = [0.001, 0.1, 0.2]
colors = ['blue', 'green', 'orange']
labels = ['Slow Convergence', 'Fast Convergence', 'Oscillation/Divergence']

# Run gradient descent for each learning rate
for learn_rate, color, label in zip(learning_rates, colors, labels):
    aa = initial_position.copy()
    delta = np.inf
    step_count = 0
    ax2.scatter(aa[0], aa[1], penalty(aa[0], aa[1]), c=color, s=100, marker='*', label=label)
    
    # Update vector aa
    while delta > epsilon:
        # Gradient Descent
        aa_next = aa - learn_rate * grad(aa)
        # Plot the animation
        ax2.plot([aa[0], aa_next[0]], [aa[1], aa_next[1]], [penalty(aa[0], aa[1]), penalty(aa_next[0], aa_next[1])], 'ko-', color=color)
        delta = np.linalg.norm(aa - aa_next)
        aa = aa_next
        step_count += 1
        if step_count >= 1000:  # to break the loop in case of divergence
            break
    print('Optimal result for learning rate', learn_rate, ':', aa)
    ax2.scatter(aa[0], aa[1], penalty(aa[0], aa[1]), c=color, s=100, marker='*')

plt.legend()
plt.show()
print('Step Count:', step_count)
