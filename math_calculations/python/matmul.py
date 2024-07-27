class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows, self.columns = self.get_dimensions()

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

    def __repr__(self):
        return repr(f"[Matrix] rows: {self.rows}, columns: {self.columns}, data: {self.data}")

def matmul(a: Matrix, b: Matrix) -> Matrix:
    if a.columns != b.rows:
        raise Exception("Columns in first matrix must equal the rows in second matrix")
    
    # Output matrix is product of rows of a and columns of b
    rows = a.rows
    columns = b.columns

    # Take all the elements in the first row and multiply it by the elements in the first column
    # Row * Column
    tmp = 0

    ab = []

    if __debug__:
        print("a", a)
        print("b", b)

    for index, row in enumerate(a.data):
        print("row index", index)
        print("row", row)
        r = []
        for index, column in enumerate(b.data):
            print("column index", index)
            print("column", column)
            r.append(row[0] * column)
        ab.append(r)
        print("ab", ab)

    return Matrix(ab)