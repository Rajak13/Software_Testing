# White-Box Testing

White-box testing is a software testing technique where the internal structure, design, and implementation of the software are known to the tester. The tester has access to the source code and uses this knowledge to design test cases.

## Key Characteristics
- Tests internal structure and logic
- Requires programming knowledge
- Focuses on code coverage
- Tests individual components

## Coverage Criteria

### 1. Statement Coverage
Ensures that each statement in the code is executed at least once.

**Example:**
```python
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'
```
To achieve statement coverage, we need test cases that:
- Score >= 90
- 80 <= Score < 90
- Score < 80

### 2. Branch Coverage
Ensures that each branch of every control structure is executed.

**Example:**
For the same function, we need test cases that:
- Score >= 90 (True branch)
- Score < 90 (False branch)
- Score >= 80 (True branch)
- Score < 80 (False branch)

### 3. Path Coverage
Ensures that all possible paths through the code are executed.

**Example:**
For a function with multiple conditions:
```python
def process_data(x, y):
    if x > 0:
        if y > 0:
            return "First quadrant"
        else:
            return "Fourth quadrant"
    else:
        if y > 0:
            return "Second quadrant"
        else:
            return "Third quadrant"
```
We need test cases for all four possible paths.

## Advantages
- Thorough testing of code
- Can find hidden errors
- Optimizes code
- Helps in understanding the code

## Disadvantages
- Requires programming knowledge
- Time-consuming
- May miss functional requirements
- Can be complex for large systems

## Tools
- Coverage.py for code coverage
- Pytest for test execution
- Radon for cyclomatic complexity

## Practical Example
See the examples in the `examples/white-box/` directory for Python implementations of these techniques. 