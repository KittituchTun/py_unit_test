"""
A simple calculator module for demonstrating unit testing in Python 3.8.
"""

class Calculator:
    """A simple calculator class with basic mathematical operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        return base ** exponent
    
    def square_root(self, number):
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def find_max_in_list(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        raise ValueError("Cannot find max in empty list")
    return max(numbers)