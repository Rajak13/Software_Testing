def calculate_discount(age: int) -> float:
    """
    Calculate discount based on age.
    Rules:
    - Under 18: No discount
    - 18-25: 10% discount
    - 26-60: 5% discount
    - Over 60: 15% discount
    """
    if age < 18:
        return 0.0
    elif 18 <= age <= 25:
        return 0.1
    elif 26 <= age <= 60:
        return 0.05
    else:
        return 0.15

# Test cases using equivalence partitioning
def test_equivalence_partitioning():
    # Test case 1: Under 18 (Invalid partition)
    assert calculate_discount(15) == 0.0
    
    # Test case 2: 18-25 (Valid partition)
    assert calculate_discount(20) == 0.1
    
    # Test case 3: 26-60 (Valid partition)
    assert calculate_discount(40) == 0.05
    
    # Test case 4: Over 60 (Valid partition)
    assert calculate_discount(65) == 0.15
    
    # Test case 5: Boundary value 18
    assert calculate_discount(18) == 0.1
    
    # Test case 6: Boundary value 25
    assert calculate_discount(25) == 0.1
    
    # Test case 7: Boundary value 26
    assert calculate_discount(26) == 0.05
    
    # Test case 8: Boundary value 60
    assert calculate_discount(60) == 0.05

if __name__ == "__main__":
    test_equivalence_partitioning()
    print("All tests passed!") 