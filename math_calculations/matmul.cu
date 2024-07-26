#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <cuda.h>
#include <cuda_runtime.h>

#define N 2
#define DEBUG

__global__ void matmul(float* out, float* arr_1, float* arr_2, int n) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row < n && col < n) {
        float value = 0;
        for (int k = 0; k < n; ++k) {
            value += arr_1[row * n + k] * arr_2[k * n + col];
        }
        out[row * n + col] = value;
    }
}

bool is_matrix_equal(float arr_1[N][N], float arr_2[N][N]) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            #ifdef DEBUG 
                printf("arr1[%d][%d]: %f, arr2[%d][%d]: %f \n", i, j, arr_1[i][j], i, j, arr_2[i][j]);
            #endif 
            if (arr_1[i][j] != arr_2[i][j]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    // Host variables
    float array_1[N][N] = {{1, 2}, {3, 4}};
    float array_2[N][N] = {{5, 6}, {7, 8}};
    float out[N][N] = {0};

    // Device variables
    float* d_array_1;
    float* d_array_2;
    float* d_out;

    // Allocate device memory
    cudaMalloc((void**)&d_array_1, N * N * sizeof(float));
    cudaMalloc((void**)&d_array_2, N * N * sizeof(float));
    cudaMalloc((void**)&d_out, N * N * sizeof(float));

    // Transfer input data from host to device memory
    cudaMemcpy(d_array_1, array_1, N * N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_array_2, array_2, N * N * sizeof(float), cudaMemcpyHostToDevice);

    // Executing kernel
    dim3 threadsPerBlock(N, N);
    dim3 numBlocks(1, 1);
    matmul<<<numBlocks, threadsPerBlock>>>(d_out, d_array_1, d_array_2, N);

    // Transfer output data from device to host memory
    cudaMemcpy(out, d_out, N * N * sizeof(float), cudaMemcpyDeviceToHost);

    // Verification
    float array_expected[N][N] = {{19, 22}, {43, 50}};
    assert(is_matrix_equal(out, array_expected) == true);

    // Deallocate device memory
    cudaFree(d_array_1);
    cudaFree(d_array_2);
    cudaFree(d_out);

    return 0;
}
