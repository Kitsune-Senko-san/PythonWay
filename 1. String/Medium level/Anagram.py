"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not.
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
For example, act and tac are an anagram of each other.

Example 1:
Input:
    a = geeksforgeeks, b = forgeeksgeeks
Output:
    YES
Explanation:
    Both the string have same characters with same frequency. So, both are anagrams.

Example 2:
Input:
    a = allergy, b = allergic
Output:
    NO
Explanation:
    Characters in both the strings are not same, so they are not anagrams.
"""

a = "geeksforgeeks"
b = "forgeeksgeeks"


def isAnagram():
    if len(a) == len(b):        # if the strings are not of the same length, they cannot be the same
        a_sorted = ''.join(sorted(a))
        b_sorted = ''.join(sorted(b))
        if a_sorted == b_sorted:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


isAnagram()
