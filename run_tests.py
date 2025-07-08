#!/usr/bin/env python3
"""
Test runner script demonstrating different ways to run unit tests in Python 3.8.
"""

import unittest
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_all_tests():
    """Run all tests with detailed output."""
    print("=" * 60)
    print("Running all unit tests with high verbosity")
    print("=" * 60)
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("Test Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    print("=" * 60)
    
    return result

def run_specific_test_class():
    """Run tests from a specific test class."""
    print("\n" + "=" * 60)
    print("Running only Calculator tests")
    print("=" * 60)
    
    from test_calculator import TestCalculator
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result

def run_specific_test_method():
    """Run a specific test method."""
    print("\n" + "=" * 60)
    print("Running only the add positive numbers test")
    print("=" * 60)
    
    from test_calculator import TestCalculator
    
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_add_positive_numbers'))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'class':
            run_specific_test_class()
        elif sys.argv[1] == 'method':
            run_specific_test_method()
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Usage: python run_tests.py [class|method]")
            sys.exit(1)
    else:
        run_all_tests()