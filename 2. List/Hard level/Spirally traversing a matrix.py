"""
Given a matrix of size row * column. Traverse the matrix in spiral form.

Example 1:
Input:
    row, column = 4, 4
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
Output:
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Example 2:
Input:
    row, column = 3, 4
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
Output:
    1 2 3 4 8 12 11 10 9 5 6 7

Example 3:
Input:
    row, column = 2, 2
    matrix = [[1, 2],
              [3, 4]]
Output:
    1 2 4 3
"""


def spirallyTraverse(matrix, row, column):
    row_start, column_start = 0, 0
    row_end = row - 1
    column_end = column - 1
    while row_start <= row_end and column_start <= column_end:
        for i in range(column_start, column_end + 1):  # top side
            print(matrix[row_start][i], end=' ')
        row_start += 1

        for i in range(row_start, row_end + 1):  # right side
            print(matrix[i][column_end], end=' ')
        column_end -= 1

        if row_start <= row_end:  # bottom side
            for i in range(column_end, column_start - 1, -1):
                print(matrix[row_end][i], end=' ')
            row_end -= 1

        if column_start <= column_end:  # left side
            for i in range(row_end, row_start - 1, -1):
                print(matrix[i][column_start], end=' ')
            column_start += 1
    print()


row, column = 4, 4
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

spirallyTraverse(matrix, row, column)

row, column = 3, 4
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

spirallyTraverse(matrix, row, column)

row, column = 2, 2
matrix = [[1, 2],
          [3, 4]]

spirallyTraverse(matrix, row, column)
