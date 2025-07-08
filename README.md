# Python 3.8 Unit Testing Example

This repository demonstrates comprehensive unit testing patterns and best practices for Python 3.8 using the built-in `unittest` framework.

## Files Overview

- **`calculator.py`** - A sample calculator module with various mathematical operations
- **`test_calculator.py`** - Comprehensive unit tests demonstrating various testing concepts
- **`run_tests.py`** - Test runner script showing different ways to execute tests

## Key Testing Concepts Demonstrated

### 1. Basic Test Structure
- Test class inheritance from `unittest.TestCase`
- Test method naming convention (`test_*`)
- Proper test documentation

### 2. Setup and Teardown
- `setUp()` - Runs before each test method
- `tearDown()` - Runs after each test method
- `setUpClass()` - Runs once before all tests in a class
- `tearDownClass()` - Runs once after all tests in a class

### 3. Assertion Methods
- `assertEqual()` / `assertNotEqual()`
- `assertTrue()` / `assertFalse()`
- `assertIsNone()` / `assertIsNotNone()`
- `assertIsInstance()` / `assertNotIsInstance()`
- `assertIn()` / `assertNotIn()`
- `assertGreater()` / `assertLess()` / `assertGreaterEqual()` / `assertLessEqual()`
- `assertAlmostEqual()` - For floating point comparisons
- `assertRaises()` - For exception testing
- `assertRegex()` - For pattern matching
- `assertCountEqual()` - For comparing sequences regardless of order

### 4. Exception Testing
```python
with self.assertRaises(ValueError) as context:
    self.calc.divide(10, 0)
self.assertEqual(str(context.exception), "Cannot divide by zero")
```

### 5. Subtests for Parameterized Testing
```python
for base, exponent, expected in test_cases:
    with self.subTest(base=base, exponent=exponent):
        result = self.calc.power(base, exponent)
        self.assertEqual(result, expected)
```

### 6. Test Skipping and Expected Failures
- `@unittest.skip()` - Skip a test unconditionally
- `@unittest.skipIf()` - Skip a test conditionally
- `@unittest.expectedFailure` - Mark a test as expected to fail

## Running the Tests

### Method 1: Direct execution
```bash
python test_calculator.py
```

### Method 2: Using unittest module
```bash
python -m unittest test_calculator.py -v
```

### Method 3: Test discovery
```bash
python -m unittest discover -v
```

### Method 4: Using the custom runner
```bash
# Run all tests
python run_tests.py

# Run specific test class
python run_tests.py class

# Run specific test method
python run_tests.py method
```

### Method 5: Run specific test class or method
```bash
# Run specific test class
python -m unittest test_calculator.TestCalculator -v

# Run specific test method
python -m unittest test_calculator.TestCalculator.test_add_positive_numbers -v
```

## Test Organization

The tests are organized into three main classes:

1. **`TestCalculator`** - Tests for the Calculator class methods
2. **`TestUtilityFunctions`** - Tests for standalone utility functions
3. **`TestAdvancedFeatures`** - Demonstrates advanced testing features

## Best Practices Demonstrated

1. **Descriptive Test Names** - Each test method clearly describes what it tests
2. **One Assertion Per Concept** - Tests focus on a single behavior
3. **Edge Case Testing** - Tests include boundary conditions and error cases
4. **Proper Exception Testing** - Validates both that exceptions are raised and their messages
5. **Floating Point Comparison** - Uses `assertAlmostEqual()` for floating point numbers
6. **Test Independence** - Each test can run independently
7. **Clear Documentation** - Tests are well-documented with docstrings

## Python 3.8 Specific Features

This example uses Python 3.8 compatible syntax and features:
- f-string formatting
- Type hints (where appropriate)
- Modern exception handling
- Built-in unittest framework capabilities

## Expected Output

When running the tests, you should see output similar to:
```
test_add_positive_numbers (test_calculator.TestCalculator) ... ok
test_divide_by_zero_raises_exception (test_calculator.TestCalculator) ... ok
test_factorial_positive_numbers (test_calculator.TestUtilityFunctions) ... ok
...
----------------------------------------------------------------------
Ran 25 tests in 0.012s

OK (skipped=2, expected failures=1)
```

This example provides a solid foundation for understanding unit testing in Python 3.8 and can be adapted for your specific testing needs.
