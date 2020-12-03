import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense




#Load dataset
dataset=pd.read_csv('cars.csv')
X=dataset.iloc[:,0:5].values
y=dataset.iloc[:,5].values
print("X:")
print(X)
print("\ny:")
print(y)


# Split the data in training set and test set
X_train, X_test, y_train, y_test = train_test_split(xscale, yscale, test_size = 0.2, random_state=5)


# Print the shapes of the new X objects
print("\nTraining set dimensions (X_train):")
print(X_train.shape)
print("\nTest set dimensions (X_test):")
print(X_test.shape)

# Print the shapes of the new y objects
print("\nTraining set dimensions (y_train):")
print(y_train.shape)
print("\nTest set dimensions (y_test):")
print(y_test.shape)


# TODO: Create the model


# TODO: Evaluate model

