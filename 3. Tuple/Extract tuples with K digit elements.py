"""
Given a list of tuples, extract all tuples having K digit elements.

Example 1:
Input :
    K = 2
    list_test = [(54, 2), (34, 55), (2, 3), (12, 45), (78,)]
Output :
    (34, 55) (12, 45) (78,)
Explanation : All tuples have numbers with 2 digits.

Example 2:
Input:
    K = 3
    list_test = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )]
Output:
    (782,)
Explanation : All tuples have numbers with 3 digits.
"""


def digit_elements(list_test, K):
    for sub_list in list_test:
        if all(len(str(element)) == K for element in sub_list):
            print(sub_list, end=' ')
    print()


def test_digit_elements():
    K = 2
    list_test = [(54, 2), (34, 55), (2, 3), (12, 45), (78,)]
    digit_elements(list_test, K)

    K = 3
    list_test = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )]
    digit_elements(list_test, K)


test_digit_elements()
