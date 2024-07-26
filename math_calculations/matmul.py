class Matrix:
    def __init__(self, data):
        self.data = data

    def get_dimensions(self):
        if not self.data:  # Check if the matrix is empty
            return 0, 0

        if isinstance(self.data[0], list):  # If the first element is a list, it's a 2D matrix
            num_rows = len(self.data)
            num_columns = len(self.data[0]) if num_rows > 0 else 0
        else:  # Otherwise, it's a 1D list
            num_rows = 1
            num_columns = len(self.data)
        
        return num_rows, num_columns

a = Matrix([2,5,6])
b = Matrix([[3], [4], [-5]])

print(a.get_dimensions())
print(b.get_dimensions())

def matmul(a, b) -> Matrix:
    ## columns in first matrix must equal the rows in second matrix
    pass

matmul(a, b)