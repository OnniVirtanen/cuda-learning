import unittest
from matmul import Matrix, matmul

class TestMatrices(unittest.TestCase):
    def est_multiply_matrices_1x1_output(self):
        a = Matrix([2,5,6])
        b = Matrix([[3], [4], [-5]])

        ab = matmul(a, b)

        self.assertEqual(ab.data[0], -4)

    def test_multiply_matrices_3x3_output(self):
        a = Matrix([2,5,6])
        b = Matrix([[3], [4], [-5]])
        expected = Matrix([[6, 15, 18], [8, 20, 24], [-10, -25, -30]])

        ba = matmul(b, a)

        print("output", ba)
        print("expected", expected)

        self.assertEqual(ba, expected)
        

    def est_matrix_dimensions(self):
        a = Matrix([2,5,6])
        b = Matrix([[3], [4], [-5]])

        self.assertEqual(a.get_dimensions(), (1, 3))
        self.assertEqual(b.get_dimensions(), (3, 1))

if __name__ == '__main__':
    unittest.main()