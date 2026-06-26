import random


def create_matrix(n, m):
    return [[random.randint(-200, 200) for _ in range(m)] for _ in range(n)]


def add_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result
