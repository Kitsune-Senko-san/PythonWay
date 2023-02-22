'''
Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the
array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1.
For example, next greater of the last element is always -1.

Example 1:
Input:
    N = 4, arr = [1, 3, 2, 4]
Output:
    3 4 4 -1
Explanation:
In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist, it is -1.

Example 2:
Input:
    N = 5, arr = [6, 8, 0, 1, 3]
Output:
    8 -1 1 3 -1
Explanation:
In the array, the next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1,
for 1 it is 3 and then for 3 there is no larger element on right and hence -1.
'''


def nextLargerElement(N, arr):
    i, j = 0, 0
    result_list = []
    for char in arr:
        i += 1          # loop iterations
        while j < N:
            if i == N:                      # the last element is always equal to 1
                result_list.append(-1)
            if arr[j] == char:
                pass
            else:
                if char < arr[j]:
                    result_list.append(arr[j])
                    break
                elif char == max(arr):      # if this is the largest number in the list, it is -1
                    result_list.append(-1)
                    break
            j += 1              # go through all the values in the loop
        j = i
    return print(*result_list)


arr = [1, 3, 2, 4]
nextLargerElement(4, arr)

arr = [6, 8, 0, 1, 3]
nextLargerElement(5, arr)

arr = [1, 3, 5, 2, 4]
nextLargerElement(5, arr)
