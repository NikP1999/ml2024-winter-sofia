class DataHandler:
    def __init__(self):
        self.numbers = []

    def insert_numbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def find_index(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        return -1
