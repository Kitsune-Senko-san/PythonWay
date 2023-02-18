"""
Write a program to Validate an IPv4 Address.
A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255.
Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255).
Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Example 1:
Input:
    IPv4 address = 222.111.111.111
Output:
    Valid

Example 2:
Input:
    IPv4 address = 5555..555
Output:
    No valid
"""

string = input("IPv4 address = ")


def isValid():
    str_list = string.split(".")    # split the string into a list by the delimiter .
    for i in str_list:
        if len(i) > 1 and int(i[0]) == 0:       # additional leading zeroes will be considered invalid (0.01.0.0)
            print("No valid")
            break
        elif 0 <= int(i) <= 255 and 1 <= len(i) <= 3:       # check for compliance (0-255).(0-255).(0-255).(0-255)
            continue
        else:
            print("No valid")
            break
    else:
        print("Valid")


isValid()
