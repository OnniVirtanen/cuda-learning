class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows, self.columns = self.get_dimensions()

    def __repr__(self):
        return repr(f"[Matrix] rows: {self.rows}, columns: {self.columns}, data: {self.data}")

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data and self.rows == other.rows and self.columns == other.columns
        return NotImplemented

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
    
    @staticmethod
    def initialize_matrix(rows: int, columns: int):
        matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                column = []
                row.append(column)
            matrix.append(row)
        return Matrix(matrix)
    
# Iterative matrix multiplication algorithm
def matmul(a: Matrix, b: Matrix) -> Matrix:
    assert isinstance(a, Matrix) and isinstance(b, Matrix)
    if __debug__:
        print(f"Matrix multiplication \n in a: {a} \n in b: {b}")
    if a.columns != b.rows:
        raise Exception("Columns in first matrix must equal the rows in second matrix")

    # Output matrix is product of rows of a and columns of b
    n = a.rows
    m = a.columns # Same as a.rows
    p = b.columns
    C = Matrix.initialize_matrix(n, p)

    for i in range(n):
        for j in range(p):
            sum = 0
            for k in range(m):
                sum += a.data[i][k] * b.data[k][j]
            C.data[i][j] = sum

    if __debug__:
        print(f" out C: {C}")

    return C