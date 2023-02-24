"""
Given a boolean 2D array of n x m dimensions where each row is sorted.
Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:
Input:
    N = 4 , M = 4
    array = [[0, 1, 1, 1],
             [0, 0, 1, 0],
             [1, 1, 1, 1],
             [1, 1, 0, 0]]
Output:
    2

Example 2:
Input:
    N = 3, M = 3
    array = [[0, 0, 1],
             [0, 1, 0],
             [1, 0, 0]]
Output:
    0 1 2

Example 3:
Input:
    N = 2, M = 2
    array = [[0, 1],
             [0, 0]]
Output:
    0
"""


def rowWithMax1s(array, N, M, check=1):
    result_list = []
    while check > 0:
        for i in range(N):
            if array[i].count(1) == M:
                result_list.append(i)
                check = 0
                continue
        else:
            M -= 1
            continue
    return print(*result_list)


N, M = 4, 4
array = [[0, 1, 1, 1],
         [0, 0, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
rowWithMax1s(array, N, M)

N, M = 3, 3
array = [[0, 0, 1],
         [0, 1, 0],
         [1, 0, 0]]
rowWithMax1s(array, N, M)

N, M = 2, 2
array = [[0, 1],
         [0, 0]]
rowWithMax1s(array, N, M)
