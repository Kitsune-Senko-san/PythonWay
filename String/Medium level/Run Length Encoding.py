"""
Given a string, Your task is to complete the function encode that returns the run length encoded string for the given string.
e.g. if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.

Example 1:
Input:
    string = aaaabbbccc
Output:
    a4b3c3
Explanation:
    a repeated 4 times consecutively b 3 times, c also 3 times.

Example 2:
Input:
    string = abbbcdddd
Output:
    a1b3c1d4
"""

string = "wwwwaaadexxxxxx"


def encode():
    i = 0
    while i != len(string):
        count_letter = string.count(string[i])
        print(string[i], count_letter, end='', sep='')
        i += count_letter


encode()
