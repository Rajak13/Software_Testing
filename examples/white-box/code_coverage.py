def calculate_tax(income: float, age: int) -> float:
    """
    Calculate tax based on income and age.
    Rules:
    - Basic tax rate: 20%
    - Senior discount (age >= 65): 5% reduction
    - High income surcharge (income > 100000): 5% increase
    """
    tax_rate = 0.20
    
    # Apply senior discount
    if age >= 65:
        tax_rate -= 0.05
    
    # Apply high income surcharge
    if income > 100000:
        tax_rate += 0.05
    
    return income * tax_rate

# Test cases for different coverage criteria
def test_statement_coverage():
    # This test covers all statements
    assert calculate_tax(50000, 30) == 10000  # Basic case
    assert calculate_tax(50000, 70) == 7500   # Senior discount
    assert calculate_tax(150000, 30) == 37500 # High income surcharge
    assert calculate_tax(150000, 70) == 30000 # Both conditions

def test_branch_coverage():
    # Test all branches
    # Branch 1: age < 65
    assert calculate_tax(50000, 30) == 10000
    # Branch 2: age >= 65
    assert calculate_tax(50000, 70) == 7500
    # Branch 3: income <= 100000
    assert calculate_tax(50000, 30) == 10000
    # Branch 4: income > 100000
    assert calculate_tax(150000, 30) == 37500

def test_path_coverage():
    # Test all possible paths
    # Path 1: age < 65, income <= 100000
    assert calculate_tax(50000, 30) == 10000
    # Path 2: age < 65, income > 100000
    assert calculate_tax(150000, 30) == 37500
    # Path 3: age >= 65, income <= 100000
    assert calculate_tax(50000, 70) == 7500
    # Path 4: age >= 65, income > 100000
    assert calculate_tax(150000, 70) == 30000

if __name__ == "__main__":
    test_statement_coverage()
    test_branch_coverage()
    test_path_coverage()
    print("All tests passed!") 