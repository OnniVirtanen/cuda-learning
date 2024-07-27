import unittest
from matmul import Matrix, matmul

class TestMatrices(unittest.TestCase):
    def test_multiply_matrices(self):
        a = Matrix([2,5,6])
        b = Matrix([[3], [4], [-5]])

        ab = matmul(a, b)

        self.assertEqual(ab.data[0], -4)

    def test_matrix_dimensions(self):
        a = Matrix([2,5,6])
        b = Matrix([[3], [4], [-5]])

        self.assertEqual(a.get_dimensions(), (1, 3))
        self.assertEqual(b.get_dimensions(), (3, 1))

if __name__ == '__main__':
    unittest.main()