#!/usr/bin/env python3
""" Divide module """
from typing import Union


def division(dividend: float, divisor: float,
             operation: str = 'float') -> Union[float, int]:
    """
    Divides the dividend by the divisor based on the specified operation.

    Args:
        dividend: The number to be divided.
        divisor: The number by which the dividend is to be divided.
        operation: The type of division operation
                   ('float', 'integer', 'modulo').
                   Defaults to 'float'.

    Returns:
        The result of the division operation.

    Raises:
        ZeroDivisionError: If the divisor is zero.
        ValueError: If the operation is invalid.
    """

    if divisor == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    if operation == 'float':
        return dividend / divisor
    elif operation == 'integer':
        return dividend // divisor
    else:
        raise ValueError(f"Unknown operation '{operation}'."
                         "Use 'float', 'integer', or 'modulo'.")


def main():
    """
    Main function for testing the division function.
    """
    dividend = float(input("Enter dividend: "))
    divisor = float(input("Enter divisor: "))
    operation = input("Enter operation (float, integer): ")

    try:
        result = division(dividend, divisor, operation)
        print("Result:", result)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()