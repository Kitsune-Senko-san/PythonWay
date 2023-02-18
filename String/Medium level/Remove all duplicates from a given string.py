"""
Given a string Str which may contains lowercase and uppercase characters.
The task is to remove all duplicate characters from the string and find the resultant string.
The order of remaining characters in the output should be same as in the original string.

Example 1:
Input:
    string = geeksforgeeks
Output:
    geksfor
Explanation:
    After removing duplicate characters such as e, k, g, s, we have string as "geksfor".

Example 2:
Input:
    string = HappyNewYear
Output:
    HapyNewYr
Explanation:
    After removing duplicate characters such as p, e, a, we have string as "HapyNewYr".
"""

string = "HappyNewYear"


def removeDuplicates():
    result = ''
    for char in string:
        if char not in result:      # letters will be added without repetition, regardless of case
            result += char
    print(result)


removeDuplicates()
