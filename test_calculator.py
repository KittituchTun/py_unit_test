"""
Unit tests for the calculator module - Python 3.8 example.

This file demonstrates various unit testing concepts:
- Basic test methods
- Testing exceptions
- Setup and teardown methods
- Different assertion methods
- Subtests for parameterized testing
- Edge case testing
"""

import unittest
import math
from calculator import Calculator, is_even, factorial, find_max_in_list


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
        print(f"Running test: {self._testMethodName}")
    
    def tearDown(self):
        """Clean up after each test method."""
        self.calc = None
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_add_mixed_numbers(self):
        """Test addition with mixed positive and negative numbers."""
        result = self.calc.add(-2, 3)
        self.assertEqual(result, 1)
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        result = self.calc.add(5, 0)
        self.assertEqual(result, 5)
    
    def test_add_floats(self):
        """Test addition with floating point numbers."""
        result = self.calc.add(2.5, 3.7)
        self.assertAlmostEqual(result, 6.2, places=1)
    
    def test_subtract(self):
        """Test subtraction operation."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
    
    def test_multiply(self):
        """Test multiplication operation."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)
    
    def test_divide(self):
        """Test division operation."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero_raises_exception(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_returns_float(self):
        """Test that division always returns a float."""
        result = self.calc.divide(7, 2)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 3.5)
    
    def test_power(self):
        """Test power operation."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
    
    def test_power_edge_cases(self):
        """Test power operation with edge cases using subtests."""
        test_cases = [
            (5, 0, 1),      # Any number to power 0 equals 1
            (0, 5, 0),      # 0 to any positive power equals 0
            (2, -2, 0.25),  # Negative exponent
            (-2, 3, -8),    # Negative base with odd exponent
            (-2, 2, 4),     # Negative base with even exponent
        ]
        
        for base, exponent, expected in test_cases:
            with self.subTest(base=base, exponent=exponent):
                result = self.calc.power(base, exponent)
                self.assertEqual(result, expected)
    
    def test_square_root(self):
        """Test square root operation."""
        result = self.calc.square_root(9)
        self.assertEqual(result, 3.0)
    
    def test_square_root_of_negative_raises_exception(self):
        """Test that square root of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.square_root(-4)
        
        self.assertIn("Cannot calculate square root of negative number", 
                     str(context.exception))
    
    def test_square_root_precision(self):
        """Test square root with floating point precision."""
        result = self.calc.square_root(2)
        self.assertAlmostEqual(result, math.sqrt(2), places=10)


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_is_even_with_even_numbers(self):
        """Test is_even function with even numbers."""
        even_numbers = [0, 2, 4, 6, 8, 100, -2, -4]
        
        for number in even_numbers:
            with self.subTest(number=number):
                self.assertTrue(is_even(number), 
                              f"{number} should be even")
    
    def test_is_even_with_odd_numbers(self):
        """Test is_even function with odd numbers."""
        odd_numbers = [1, 3, 5, 7, 9, 101, -1, -3]
        
        for number in odd_numbers:
            with self.subTest(number=number):
                self.assertFalse(is_even(number), 
                               f"{number} should be odd")
    
    def test_factorial_base_cases(self):
        """Test factorial function with base cases."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_positive_numbers(self):
        """Test factorial function with positive numbers."""
        test_cases = [
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = factorial(n)
                self.assertEqual(result, expected)
    
    def test_factorial_negative_raises_exception(self):
        """Test that factorial of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        
        self.assertEqual(str(context.exception), 
                        "Factorial is not defined for negative numbers")
    
    def test_find_max_in_list(self):
        """Test finding maximum in a list."""
        test_cases = [
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 5),
            ([1, 5, 2, 4, 3], 5),
            ([-1, -2, -3], -1),
            ([0], 0),
            ([1.5, 2.7, 1.1], 2.7),
        ]
        
        for numbers, expected in test_cases:
            with self.subTest(numbers=numbers):
                result = find_max_in_list(numbers)
                self.assertEqual(result, expected)
    
    def test_find_max_empty_list_raises_exception(self):
        """Test that finding max in empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            find_max_in_list([])
        
        self.assertEqual(str(context.exception), 
                        "Cannot find max in empty list")


class TestAdvancedFeatures(unittest.TestCase):
    """Demonstrate advanced testing features."""
    
    @classmethod
    def setUpClass(cls):
        """Set up class fixtures before any tests in this class."""
        print("Setting up TestAdvancedFeatures class")
        cls.shared_resource = "This is shared across all test methods"
    
    @classmethod
    def tearDownClass(cls):
        """Clean up class fixtures after all tests in this class."""
        print("Tearing down TestAdvancedFeatures class")
        cls.shared_resource = None
    
    def test_assertions_demo(self):
        """Demonstrate various assertion methods."""
        # Basic equality
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)
        
        # Boolean assertions
        self.assertTrue(True)
        self.assertFalse(False)
        
        # None assertions
        self.assertIsNone(None)
        self.assertIsNotNone("not none")
        
        # Type assertions
        self.assertIsInstance(42, int)
        self.assertNotIsInstance(42, str)
        
        # Membership assertions
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
        
        # Comparison assertions
        self.assertGreater(5, 3)
        self.assertLess(3, 5)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(3, 5)
        
        # String assertions
        self.assertRegex("hello world", r"hello.*world")
        self.assertCountEqual([1, 2, 3], [3, 2, 1])  # Same elements, any order
    
    def test_with_mock_example(self):
        """Example of testing that would benefit from mocking."""
        # This is a placeholder showing where you might use mocks
        # In Python 3.8, you would use unittest.mock for this
        calc = Calculator()
        result = calc.add(1, 1)
        self.assertEqual(result, 2)
    
    @unittest.skip("Demonstrating test skipping")
    def test_skipped_test(self):
        """This test will be skipped."""
        self.fail("This test should not run")
    
    @unittest.skipIf(True, "Conditionally skipped test")
    def test_conditionally_skipped(self):
        """This test is conditionally skipped."""
        self.fail("This test should not run")
    
    @unittest.expectedFailure
    def test_expected_failure(self):
        """This test is expected to fail."""
        self.assertEqual(1, 2, "This is expected to fail")


if __name__ == '__main__':
    # Configure test runner
    unittest.main(verbosity=2, buffer=True)