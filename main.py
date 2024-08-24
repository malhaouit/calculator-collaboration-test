#!/usr/bin/env python3
"""
The main program to run the simple calculator application.
"""
from operations.sine import sine


def main():
    """
    The entry point of the simple calculator application to execute the
    specified operation.
    """
    print("Simple Calculator")
    print("-----------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Modulus")
    print("9. Logarithm")
    print("10. Exponential")
    print("11. Absolute")
    print("12. Sine")
    print("13. Cosine")
    print("14. Tangent")

    # Gets the input number from the user to select the specified operation
    choice = input("Select operation: ")

    while choice not in [
            '1', '2', '3', '4', '5', '7', '8',
            '9', '10', '11', '12', '13', '14']:
        choice = input("Please select an existing operation: ")

    if choice == '1':
        print('not implemented yet...')
    elif choice == '2':
        print('not implemented yet...')
    elif choice == '2':
        print('not implemented yet...')
    elif choice == '3':
        print('not implemented yet...')
    elif choice == '4':
        print('not implemented yet...')
    elif choice == '5':
        print('not implemented yet...')
    elif choice == '6':
        print('not implemented yet...')
    elif choice == '7':
        print('not implemented yet...')
    elif choice == '8':
        print('not implemented yet...')
    elif choice == '9':
        print('not implemented yet...')
    elif choice == '10':
        print('not implemented yet...')
    elif choice == '11':
        print('not implemented yet...')
    elif choice == '12':
        num = float(input("Enter the number in degrees: "))
        print("Result: {}".format(sine(num)))
    elif choice == '13':
        print('not implemented yet...')
    elif choice == '14':
        print('not implemented yet...')


if __name__ == "__main__":
    main()
