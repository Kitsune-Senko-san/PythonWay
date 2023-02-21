"""
Given a number 'N'. The task is to find the Nth number whose each digit is a prime number i.e 2, 3, 5, 7.
In other words you have to find nth number of this sequence : 2, 3, 5, 7, 22, 23 ,.. and so on.

Example 1:
Input:
    N = 10
Output:
    33
Explanation:
    10th number in the sequence of numbers whose each digit is prime is 33.

Example 2:
Input:
    N = 21
Output:
    222
Explanation:
    21st number in the sequence of numbers whose each digit is prime is 222.
"""


def primeDigits(N):
    first_primes = [2, 3, 5, 7]         # initial primes, all other numbers will consist of them
    list_of_primes = first_primes.copy()    # copying the initial values
    counter = 0
    while counter < N:
        x = list_of_primes[counter]         # searching through the initial values and then the added ones
        for i in first_primes:          # searching for prime numbers in a loop (2, 3, 5, 7, 2, 3, 5, 7...)
            new_list_item = x * 10 + i      # forming new prime numbers from these values (22, 23, 25, 27, 32, 33, 35, 37...)
            if new_list_item not in list_of_primes:
                list_of_primes.append(new_list_item)
        counter += 1
    print(list_of_primes[counter - 1])


primeDigits(21)
