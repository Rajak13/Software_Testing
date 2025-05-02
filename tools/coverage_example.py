"""
Example demonstrating how to use coverage tools in Python.
This example shows how to:
1. Run tests with coverage
2. Generate coverage reports
3. Analyze coverage results
"""

def complex_function(x: int, y: int) -> str:
    """
    A complex function with multiple branches and conditions.
    """
    if x > 0:
        if y > 0:
            return "First quadrant"
        elif y < 0:
            return "Fourth quadrant"
        else:
            return "Positive X-axis"
    elif x < 0:
        if y > 0:
            return "Second quadrant"
        elif y < 0:
            return "Third quadrant"
        else:
            return "Negative X-axis"
    else:
        if y > 0:
            return "Positive Y-axis"
        elif y < 0:
            return "Negative Y-axis"
        else:
            return "Origin"

def test_complex_function():
    # Test cases for different quadrants
    assert complex_function(1, 1) == "First quadrant"
    assert complex_function(-1, 1) == "Second quadrant"
    assert complex_function(-1, -1) == "Third quadrant"
    assert complex_function(1, -1) == "Fourth quadrant"
    
    # Test cases for axes
    assert complex_function(1, 0) == "Positive X-axis"
    assert complex_function(-1, 0) == "Negative X-axis"
    assert complex_function(0, 1) == "Positive Y-axis"
    assert complex_function(0, -1) == "Negative Y-axis"
    
    # Test case for origin
    assert complex_function(0, 0) == "Origin"

if __name__ == "__main__":
    # Run the tests
    test_complex_function()
    print("All tests passed!")

    # Note: To run this with coverage, use:
    # coverage run coverage_example.py
    # coverage report -m
    # coverage html  # For HTML report 