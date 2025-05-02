"""
Example demonstrating cyclomatic complexity concepts.
This example shows:
1. Functions with different complexity levels
2. How to measure complexity
3. How to reduce complexity
"""

# Low complexity function (CC = 2)
def simple_addition(a: int, b: int) -> int:
    return a + b

# Medium complexity function (CC = 4)
def grade_calculator(score: int) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

# High complexity function (CC = 8)
def complex_decision(x: int, y: int, z: int) -> str:
    if x > 0:
        if y > 0:
            if z > 0:
                return "All positive"
            else:
                return "X and Y positive"
        else:
            if z > 0:
                return "X and Z positive"
            else:
                return "Only X positive"
    else:
        if y > 0:
            if z > 0:
                return "Y and Z positive"
            else:
                return "Only Y positive"
        else:
            if z > 0:
                return "Only Z positive"
            else:
                return "All negative"

# Refactored version of complex_decision (CC = 4)
def refactored_decision(x: int, y: int, z: int) -> str:
    positives = []
    if x > 0:
        positives.append("X")
    if y > 0:
        positives.append("Y")
    if z > 0:
        positives.append("Z")
    
    if not positives:
        return "All negative"
    elif len(positives) == 3:
        return "All positive"
    else:
        return " and ".join(positives) + " positive"

def test_functions():
    # Test simple_addition
    assert simple_addition(2, 3) == 5
    
    # Test grade_calculator
    assert grade_calculator(95) == 'A'
    assert grade_calculator(85) == 'B'
    assert grade_calculator(75) == 'C'
    assert grade_calculator(65) == 'F'
    
    # Test complex_decision
    assert complex_decision(1, 1, 1) == "All positive"
    assert complex_decision(1, 1, -1) == "X and Y positive"
    assert complex_decision(-1, -1, -1) == "All negative"
    
    # Test refactored_decision
    assert refactored_decision(1, 1, 1) == "All positive"
    assert refactored_decision(1, 1, -1) == "X and Y positive"
    assert refactored_decision(-1, -1, -1) == "All negative"

if __name__ == "__main__":
    test_functions()
    print("All tests passed!")
    
    # Note: To measure cyclomatic complexity, use:
    # radon cc cyclomatic_complexity.py 