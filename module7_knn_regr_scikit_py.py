# -*- coding: utf-8 -*-
"""module7_knn-regr-scikit.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m_9SCIEev26vbEx8H82yYyVrXL8lierg
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Read input N
N = int(input("Enter the number of points (N): "))

# Read input k
k = int(input("Enter the value of k: "))

# Check if k <= N
if k > N:
    print("Error: k should be less than or equal to N")
    exit()

# Read N points
points = []
for i in range(N):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    points.append([x, y])

# Convert points to numpy array
points = np.array(points)

# Split points into X and y
X = points[:, 0].reshape(-1, 1)
y = points[:, 1]


# Calculate variance of labels
variance = np.var(y)

# Create KNeighborsRegressor model
model = KNeighborsRegressor(n_neighbors=k)

# Fit the model
model.fit(X, y)

# Read input X
X_input = float(input("Enter the value of X: "))

# Predict Y
Y_pred = model.predict([[X_input]])

# Print result
print(f"The result (Y) of k-NN Regression is: {Y_pred[0]}")
print(f"Variance of labels in the training dataset: {variance}")