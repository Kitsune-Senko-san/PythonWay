"""
Given two arrays: a1 and a2. Task is to check whether a2 is a subset of a1 or not. Both the arrays can be sorted or unsorted.
You don't need to read input or print anything. Your task is to complete the function isSubset() which takes
the array a1[], a2[], as inputs and return "Yes" if arr2 is subset of arr1 else return "No" if arr2 is not subset of arr1.

Example 1:
Input:
    a1 = [11, 1, 13, 21, 3, 7]
    a2 = [11, 3, 7, 1]
Output:
    Yes

Example 2:
Input:
    a1 = [1, 2, 3, 4, 5, 6]
    a2 = [1, 2, 4]
Output:
    Yes

Example 3:
Input:
    a1 = [10, 5, 2, 23, 19]
    a2 = [19, 5, 3]
Output:
    No
"""


def isSubset(a1, a2):
    for char in a2:
        if char not in a1:
            print("No")
            break
    else:
        print("Yes")


a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]
isSubset(a1, a2)

a1 = [1, 2, 3, 4, 5, 6]
a2 = [1, 2, 4]
isSubset(a1, a2)

a1 = [10, 5, 2, 23, 19]
a2 = [19, 5, 3]
isSubset(a1, a2)
