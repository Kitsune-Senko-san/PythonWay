"""
Complete the function atoi() which takes a string as input parameter and returns integer value of it.
if the input string is not a numerical string then returns -1.
Note: You are not allowed to use inbuilt function.
Note 2: Numerical strings are the string where either every character is in between 0-9 or where the first character is '-'
and the rest all characters are in between 0-9.

Example 1:
Input:
    str = 123
Output:
    123

Example 2:
Input:
    str = 21a
Output:
    -1
Explanation: Output is -1 as all characters are not digit only.
"""


def atoi():
    try:
        string = int(input("enter number: "))
        if -1 >= string or string >= 0:
            print(string)
        else:
            print(-1)
    except ValueError:
        print(-1)


atoi()
