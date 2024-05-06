#!/usr/bin/python3
import sys

# Define a function to calculate the factorial of a number
def factorial(n):
    """
    factorial - Calculate the factorial of a given integer.
    @n: (int) The integer for which to calculate the factorial.
    Returns: integer The factorial of the input integer.
    """
    # Base case: If n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: Multiply n by the factorial of (n-1)
    else:
        return (n * factorial(n-1))
    # Get the command-line argument passed to the script and convert it to an integer
    # The first command-line argument (sys.argv[0]) is the script name itself
    # The second argument (sys.argv[1]) is the integer for which to calculate the factorial
    # Note: Error handling for missing or invalid command-line arguments is not included

f = factorial(int(sys.argv[1]))
# Print the factorial of the input integer
print(f)
