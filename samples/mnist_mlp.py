import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten the data
x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

# Define the MLP model with two ReLU layers
model = Sequential([
    Flatten(input_shape=(28 * 28,)),
    Dense(128, activation='relu'),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print('Test accuracy:', test_acc)

# Display some examples from first 20 images
print(y_train[0:20])
plt.figure(1)
for i in range(20):
    plt.subplot(2, 10, i+1)
    plt.imshow(x_train[i].reshape(28, 28), cmap = plt.cm.binary)
plt.show()
