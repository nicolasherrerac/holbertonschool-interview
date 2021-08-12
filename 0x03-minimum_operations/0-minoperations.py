#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
