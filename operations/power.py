#!/usr/bin/env python3
"""Power Module"""


def power(base, exponent):
    """
    Calculate the power of a number.

    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    for _ in range(exponent):
        result *= base
    return result


if __name__ == "__main__":
    base = 2
    exponent = -3
    print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
