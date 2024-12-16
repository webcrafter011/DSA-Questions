matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17], [19, 21, 23]]
target = 11


def searchIn(matrix, target):
    n = len(matrix)

    while len(matrix) > 1:
        midOuter = len(matrix) // 2
        if target > matrix[midOuter - 1][-1]:
            matrix = matrix[midOuter:]
        else:
            matrix = matrix[:midOuter]

    row = matrix[0]

    while len(row) > 1:
        midInner = len(row) // 2
        if target > row[midInner - 1]:
            row = row[midInner:]
        else:
            row = row[:midInner]

    if target == row[0]:
        return True

    return False


print(searchIn(matrix, target))
