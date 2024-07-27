import unittest
from matmul import Matrix, matmul

class TestMatrices(unittest.TestCase):
    def test_matrix_multiplication_1x1_output(self):
        a = Matrix([[2,5,6]])
        b = Matrix([[3], [4], [-5]])

        ab = matmul(a, b)

        self.assertEqual(ab.data[0][0], -4)

    def test_matrix_multiplications_3x3_output(self):
        a = Matrix([[2,5,6]])
        b = Matrix([[3], [4], [-5]])
        expected = Matrix([[6, 15, 18], [8, 20, 24], [-10, -25, -30]])

        ba = matmul(b, a)

        self.assertEqual(ba, expected)

    def test_matrix_multiplication_2x4_output(self):
        a = Matrix([[1, 4, -2], [3, 5, -6]])
        b = Matrix([[5, 2, 8, -1], [3, 6, 4, 5], [-2, 9, 7, -3]])
        expected = Matrix([[21, 8, 10, 25], [42, -18, 2, 40]])

        ab = matmul(a, b)

        self.assertEqual(ab, expected)
        
    def test_matrix_dimensions(self):
        a = Matrix([[2,5,6]])
        b = Matrix([[3], [4], [-5]])

        self.assertEqual(a.get_dimensions(), (1, 3))
        self.assertEqual(b.get_dimensions(), (3, 1))

if __name__ == '__main__':
    unittest.main()