
from knn_regressor import KNNRegressor  # Importing the class from the other file

def main():
    # Ask for the number of points (N)
    N = int(input("Enter a positive integer (N): "))
    
    # Ask for the value of k
    k = int(input("Enter a positive integer (k): "))
    
    # Collect the data points
    points = []
    print(f"Enter {N} (x, y) points:")
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points.append((x, y))
    
    # Initialize the KNNRegressor with the given points
    knn_regressor = KNNRegressor(points)
    
    # Ask for the input X to predict Y
    x_input = float(input("Enter the X value to predict Y: "))
    
    # Perform k-NN regression and output the result
    result = knn_regressor.knn_regression(x_input, k)
    print("Result:", result)


# Run the main program
if __name__ == "__main__":
    main()  # This is the entry point to run the code
