## This is course material for Introduction to Modern Artificial Intelligence
## Example code: mlp.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Load dependencies
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Create data
linearSeparableFlag = False
x_bias = 6

def toy_2D_samples(x_bias ,linearSeparableFlag):
    label1 = np.array([[1, 1]])
    label2 = np.array([[-1, -1]])
    array1 = np.array([[-1, 1]])
    array2 = np.array([[1, -1]])

    if linearSeparableFlag:
        samples1 = np.random.multivariate_normal([5+x_bias, 0], [[1, 0],[0, 1]], 100)
        samples2 = np.random.multivariate_normal([-5+x_bias, 0], [[1, 0],[0, 1]], 100)
        samples = np.concatenate((samples1, samples2 ), axis =0)
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
        plt.show()
    else:
        samples1 = np.random.multivariate_normal([5+x_bias, 5], [[1, 0],[0, 1]], 100)
        samples2 = np.random.multivariate_normal([-5+x_bias, -5], [[1, 0],[0, 1]], 100)
        samples3 = np.random.multivariate_normal([-5+x_bias, 5], [[1, 0],[0, 1]], 100)
        samples4 = np.random.multivariate_normal([5+x_bias, -5], [[1, 0],[0, 1]], 100)
        samples = np.concatenate((samples1, samples2, samples3, samples4 ), axis =0)
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
        plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    labels1 = np.repeat(label1, 100, axis = 0)
    labels2 = np.repeat(label2, 100, axis = 0)
    arrays1 = np.repeat(array1, 100, axis = 0)
    arrays2 = np.repeat(array2, 100, axis = 0)
    labels = np.concatenate((labels1, labels2, arrays1, arrays2 ), axis =0)
    return samples, labels

samples, labels = toy_2D_samples(x_bias ,linearSeparableFlag)

# Split training and testing set
randomOrder = np.random.permutation(400)
trainingX = samples[randomOrder[0:200], :]
trainingY = labels[randomOrder[0:200], :]
testingX = samples[randomOrder[200:400], :]
testingY = labels[randomOrder[200:400], :] # actual truth

# Build the model
model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='sigmoid', use_bias=True))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
model.fit(trainingX, trainingY, epochs=1000, batch_size=10, verbose=1, validation_split=0.2)

# Evaluate the model
ans = np.zeros((200,1))
for i in range(200):
    if (testingY[i,0] + testingY[i,1] == 0):
        ans[i] = 1 #red
    else:
        ans[i] = 0 #blue

score = 0
for i in range(200):
    predict_x = model.predict(np.array([testingX[i,:]])) 
    
    if (predict_x[0,0].round() == predict_x[0,1].round()):
        estimate = 0 #model thinks it's blue
    else:
        estimate = 1 #model thinks it's red

    if ans[i] == estimate: #comparing with actual truth
        score += 1

    if estimate == 0:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    else: 
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')

print('Test accuracy:', score/200)
plt.show()
