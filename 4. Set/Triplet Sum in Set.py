"""
Given set and an integer x. Find if there's a triplet in the array which sums up to the given integer x.

Example 1:
Input:
    x = 13
    t = {1, 4, 45, 6, 10, 8}
Output:
    The triplet {1, 4, 8} in the array sums up to 13.

Example 2:
Input:
    x = 10
    t = {1, 2, 4, 3, 6}
Output:
    The triplet {1, 3, 6} in the array sums up to 10.

Example 3:
Input:
    x = 32
    t = {3, 9, 12, 6, 10}
Output:
    It is impossible to make a triplet with the sum up to 32.
Explanation:
The maximum possible value of the triplet {9, 12, 10} will be 31.
"""


def triplet(t, x):
    result = set()
    for i in t:
        for j in t:
            for k in t:
                if i + j + k == x and i != j and i != k and j != k:
                    result.add(i)
                    result.add(j)
                    result.add(k)
                    return print(f"The triplet {result} in the array sums up to {x}.")

    print(f'It is impossible to make a triplet with the sum up to {x}.')


def find_triplet():
    x = 13
    t = {1, 4, 45, 6, 10, 8}
    triplet(t, x)

    x = 10
    t = {1, 2, 4, 3, 6}
    triplet(t, x)

    x = 32
    t = {3, 9, 12, 6, 10}
    triplet(t, x)


find_triplet()
