"""
Given an array of positive integers. Find the length of the longest sub-sequence such that elements
in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Example 1:
Input:
    t = {0, 2, 6, 1, 9, 4, 5, 3, 3}
Output:
    7 -> (0 1 2 3 4 5 6)
Explanation:
The consecutive numbers here are 0, 1, 2, 3, 4, 5, 6. These 7 numbers form the longest consecutive subsequence.

Example 2:
Input:
    t = {1, 9, 3, 10, 4, 20, 2}
Output:
    4 -> (1 2 3 4)

Example 3:
Input:
    t = {3, 9, 12, 6, 10}
Output:
    1 -> (3)
"""


def longest_subseq(t):
    count = min(t)
    check_tuple = set()
    for i in range(max(t) + 1):
        if i in t and count == i:
            check_tuple.add(i)
            count = i + 1
    subsequence = " ".join(str(x) for x in check_tuple)
    print(f"{len(check_tuple)} -> ({subsequence})")


def find_longest_subseq():
    t = {0, 2, 6, 1, 9, 4, 5, 3, 3}
    longest_subseq(t)

    t = {1, 9, 3, 10, 4, 20, 2}
    longest_subseq(t)

    t = {3, 9, 12, 6, 10}
    longest_subseq(t)


find_longest_subseq()
