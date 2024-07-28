#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>

#define TEST

#define LOG_ERROR(msg) printf("ERROR: %s\n", msg)
#define LOG_TEST(msg) printf("TEST: %s\n", msg)

typedef struct Matrix {
    float* data;
    int row_size;
    int column_size;
} matrix;

matrix* matrix_create(int row_size, int column_size) {
    matrix* m = (matrix*)malloc(sizeof(matrix));
    m->row_size = row_size;
    m->column_size = column_size;
    m->data = (float*)malloc(row_size * column_size * sizeof(float));
    return m;
}

float matrix_get_element(matrix* m, int row, int column) {
    return m->data[row * m->column_size + column];
}

void matrix_set_element(matrix* m, int row, int column, float value) {
    m->data[row * m->column_size + column] = value;
}

#ifdef DEBUG
void matrix_print(matrix* m) {
    printf("Matrix %dx%d\n", m->row_size, m->column_size);
    for (int row = 0; row < m->row_size; row++) {
        for (int column = 0; column < m->column_size; column++) {
            printf("[%.2f]", matrix_get_element(m, row, column));
        }
        printf("\n");
    }
}
#else
#define matrix_print(m) ((void)0)
#endif

matrix* matrix_multiply(matrix* a, matrix* b) {
    assert(a->column_size == b->row_size);

    #ifdef DEBUG
        printf("-in a:\n");
        matrix_print(a);
        printf("-in b:\n");
        matrix_print(b);
    #endif

    int n = a->row_size;
    int m = a->column_size;
    int p = b->column_size;
    matrix* C = matrix_create(n, p);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            float sum = 0;
            for (int k = 0; k < m; k++) {
                sum += matrix_get_element(a, i, k) * matrix_get_element(b, k, j);
            }
            matrix_set_element(C, i, j, sum);
        }
    }

    #ifdef DEBUG
        printf("-out C:\n");
        matrix_print(C);
    #endif

    return C;
}

bool is_matrix_equal(matrix* a, matrix* b) {
    assert(a != NULL && b != NULL);
    if (a->row_size != b->row_size || a->column_size != b->column_size) {
        return false;
    }
    for (int row = 0; row < a->row_size; row++) {
        for (int column = 0; column < a->column_size; column++) {
            bool equals = matrix_get_element(a, row, column) == matrix_get_element(b, row, column);
            if (!equals) {
                return false;
            }
        }
    }

    return true;
}

void matrix_free(matrix* m) {
    if (m) {
        free(m->data);
        free(m);
    }
}

#ifdef TEST
void test_matrix_multiplication_1x1_output() {
    LOG_TEST("matrix multiplication 1x1 output");

    float a[1][3] = { {2, 5, 6} };
    float b[3][1] = { {3}, {4}, {-5} };

    matrix* matrix_a = matrix_create(1, 3);
    matrix* matrix_b = matrix_create(3, 1);

    memcpy(matrix_a->data, a, sizeof(a));
    memcpy(matrix_b->data, b, sizeof(b));
    
    matrix* matrix_out = matrix_multiply(matrix_a, matrix_b);
    assert(matrix_out->data[0] == -4.0);

    matrix_free(matrix_a);
    matrix_free(matrix_b);
    matrix_free(matrix_out);
}

void test_matrix_multiplication_3x3_output() {
    LOG_TEST("matrix multiplication 3x3 output");
    
    float a[1][3] = { {2, 5, 6} };
    float b[3][1] = { {3}, {4}, {-5} };

    matrix* matrix_a = matrix_create(1, 3);
    matrix* matrix_b = matrix_create(3, 1);

    memcpy(matrix_a->data, a, sizeof(a));
    memcpy(matrix_b->data, b, sizeof(b));

    matrix* matrix_out = matrix_multiply(matrix_b, matrix_a);

    float expected[3][3] = { {6, 15, 18}, {8, 20, 24}, {-10, -25, -30} };
    matrix* matrix_expected = matrix_create(3, 3);
    memcpy(matrix_expected->data, expected, sizeof(expected));

    assert(is_matrix_equal(matrix_out, matrix_expected));

    matrix_free(matrix_a);
    matrix_free(matrix_b);
    matrix_free(matrix_out);
    matrix_free(matrix_expected);
}

void run_tests() {
    printf("--Running tests\n");
    test_matrix_multiplication_1x1_output();
    test_matrix_multiplication_3x3_output();
    printf("--Tests completed\n");
}
#endif

int main() {
    #ifdef TEST
        run_tests();
    #endif
    return 0;
}