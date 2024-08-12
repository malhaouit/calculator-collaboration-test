#!/usr/bin/env python3
"""
Factorial Module

This module provides a function to compute the factorial of a number.
"""


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input number.

    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    n = 5
    print(f"The factorial of {n} is {factorial(n)}")
