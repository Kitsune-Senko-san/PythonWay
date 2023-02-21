"""
Given a string s and an integer k, the task is to reduce the string by applying the following operation:
Choose a group of k consecutive identical characters and remove them.

Example 1:
Input:
    k = 2
    s = "geeksforgeeks"
Output:
    gksforgks
Explanation:
Modified String after each step: "geeksforgeeks" -> "gksforgks"

Example 2:
Input:
    k = 2
    s = "geegsforgeeeks"
Output:
    ggsforgeks
Explanation:
Modified String after each step: "geegsforgeeeks" -> "ggsforgeks"
"""


def reducedString(string, k):
    result_list = []
    i = 0
    while i < len(string):
        current_letter = string[i]
        counter_k = 1
        j = i + 1
        while j < len(string):
            # checking 2 letters and ignoring repetitions according to the k value
            if string[j] == current_letter and counter_k < k:
                counter_k += 1
                j += 1
            else:
                break
        if counter_k < k:
            result_list.append(current_letter)
        i = j             # starting the check from the correct value
    return ''.join(result_list)


k = 2
string = "geeksforgeeks"
print(reducedString(string, k))

k = 2
string = "geegsforgeeeks"
print(reducedString(string, k))

k = 3
string = "geeeegsforgeeeks"
print(reducedString(string, k))
