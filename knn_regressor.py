 
import numpy as np

class KNNRegressor:
    def __init__(self, points):
        self.points = np.array(points)

    def knn_regression(self, x_input, k):
        # Ensure that k is not greater than the number of points
        if k > len(self.points):
            return "Error: k cannot be greater than the number of points"
        
        # Calculate Euclidean distances between x_input and all x-coordinates in the dataset
        distances = np.abs(self.points[:, 0] - x_input)
        
        # Get the indices of the k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]
        
        # Calculate the mean Y value of the k nearest neighbors
        mean_y = np.mean(self.points[nearest_indices, 1])
        
        return mean_y
