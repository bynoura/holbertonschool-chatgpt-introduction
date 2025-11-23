#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is computed.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the number n.
             Returns 1 when n is 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
