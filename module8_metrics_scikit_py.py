# -*- coding: utf-8 -*-
"""module8_metrics-scikit.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vVbyPK-WWiibgtLNEewIcxSvYXiwskq1
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score

# Read input N
N = int(input("Enter the number of points: "))

# Initialize arrays to store ground truth and predicted labels
ground_truth = np.zeros(N, dtype=int)
predicted = np.zeros(N, dtype=int)

# Read ground truth and predicted labels for each point
for i in range(N):
    ground_truth[i] = int(input(f"Enter ground truth for point {i+1}: "))
    predicted[i] = int(input(f"Enter predicted label for point {i+1}: "))

# Calculate Precision and Recall
precision = precision_score(ground_truth, predicted, average='macro', zero_division=0)
recall = recall_score(ground_truth, predicted, average='macro', zero_division=0)


# Print Precision and Recall
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")