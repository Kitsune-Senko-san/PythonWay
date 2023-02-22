"""
Given two lists of numbers, write a program that will create a new list so that the new list contains numbers
at odd indices from the first list and even indices from the second list without repetition.
"""


def exponent(first_list, second_list):
    first_list = first_list[::2]
    second_list = second_list[1::2]
    new_list = []
    for i in range(len(first_list)):
        if first_list[i] not in new_list:
            new_list.append(first_list[i])
        else:
            continue
    for i in range(len(second_list)):
        if second_list[i] not in new_list:
            new_list.append(second_list[i])
        else:
            continue
    return new_list


first_list = [40, 45, 60, 10, 35, 20, 40, 45, 10, 10]
second_list = [10, 20, 40, 45, 25, 30, 60, 75, 35]
print(exponent(first_list, second_list))


first_list = [10, 20, 40, 45, 25, 30, 60, 75, 35]
second_list = [40, 45, 60, 10, 35, 20, 40, 45, 10, 10]
print(exponent(first_list, second_list))
