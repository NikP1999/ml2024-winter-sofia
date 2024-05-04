from module5_mod import DataHandler

data_handler = DataHandler()

N = int(input("Enter a positive integer (N): "))
data_handler.insert_numbers(N)

X = int(input("Enter the integer X to find in the list: "))
result = data_handler.find_index(X)

print(result)
