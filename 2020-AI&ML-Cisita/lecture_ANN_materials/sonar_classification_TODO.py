import numpy
import pandas
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from keras import optimizers



# load dataset
dataframe = pandas.read_csv("sonar.csv", header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:60].astype(float)
y = dataset[:,60]


# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)


# Split the data in training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, encoded_y, test_size=0.30, random_state=42)


# print the shapes of the new X objects
print("\nTraining set dimensions (X_train):")
print(X_train.shape)
print("\nTest set dimensions (X_test):")
print(X_test.shape)

# print the shapes of the new y objects
print("\nTraining set dimensions (y_train):")
print(y_train.shape)
print("\nTest set dimensions (y_test):")
print(y_test.shape)


# TODO: Create the model


# TODO: Evaluate model




