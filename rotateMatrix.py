matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotateMatrix(matrix):
    n = len(matrix)

    # transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row of the matrix
    for i in range(n):
        matrix[i].reverse()


rotateMatrix(matrix)
print(matrix)
