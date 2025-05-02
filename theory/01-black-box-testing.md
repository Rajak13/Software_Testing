# Black-Box Testing

Black-box testing is a software testing technique where the internal structure, design, and implementation of the software are not known to the tester. The tester only knows the inputs and expected outputs of the system.

## Key Characteristics
- Focuses on functional requirements
- Independent of implementation details
- Tests from the user's perspective
- Can be performed by non-technical testers

## Common Techniques

### 1. Equivalence Partitioning
Divides input data into valid and invalid partitions, where all values in a partition should be treated the same way.

**Example:**
For a function that accepts ages between 18 and 65:
- Valid partition: 18-65
- Invalid partitions: <18 and >65

### 2. Boundary Value Analysis
Tests values at the boundaries of input ranges.

**Example:**
For the same age function:
- Test values: 17, 18, 19, 64, 65, 66

### 3. Decision Table Testing
Used for testing system behavior for different input combinations.

**Example:**
For a login system:
| Username | Password | Expected Result |
|----------|----------|-----------------|
| Valid    | Valid    | Success         |
| Valid    | Invalid  | Failure         |
| Invalid  | Valid    | Failure         |
| Invalid  | Invalid  | Failure         |

## Advantages
- Tests from user perspective
- No need for programming knowledge
- Can be performed early in development
- Helps identify missing requirements

## Disadvantages
- May miss logical errors
- Can be redundant
- Limited coverage of code paths
- May not find all errors

## Practical Example
See the examples in the `examples/black-box/` directory for Python implementations of these techniques. 