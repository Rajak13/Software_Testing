"""
Example demonstrating regression testing concepts.
This example shows:
1. How to maintain test cases for existing functionality
2. How to test new changes without breaking old functionality
3. How to use pytest fixtures for regression testing
"""

import pytest

class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username: str, email: str) -> bool:
        """Original functionality"""
        if username in self.users:
            return False
        self.users[username] = {'email': email}
        return True
    
    def get_user(self, username: str) -> dict:
        """Original functionality"""
        return self.users.get(username, {})
    
    def update_user(self, username: str, new_email: str) -> bool:
        """New functionality added later"""
        if username not in self.users:
            return False
        self.users[username]['email'] = new_email
        return True

@pytest.fixture
def user_manager():
    """Fixture to create a fresh UserManager instance for each test"""
    return UserManager()

def test_original_functionality(user_manager):
    """Test original functionality"""
    # Test adding users
    assert user_manager.add_user('user1', 'user1@example.com') == True
    assert user_manager.add_user('user1', 'user1@example.com') == False  # Duplicate
    
    # Test getting users
    assert user_manager.get_user('user1') == {'email': 'user1@example.com'}
    assert user_manager.get_user('nonexistent') == {}

def test_new_functionality(user_manager):
    """Test new functionality while preserving old behavior"""
    # First ensure original functionality works
    assert user_manager.add_user('user1', 'user1@example.com') == True
    
    # Test new update functionality
    assert user_manager.update_user('user1', 'new@example.com') == True
    assert user_manager.get_user('user1') == {'email': 'new@example.com'}
    
    # Test update with nonexistent user
    assert user_manager.update_user('nonexistent', 'new@example.com') == False

def test_regression(user_manager):
    """Regression test to ensure new changes don't break old functionality"""
    # Test original add functionality
    assert user_manager.add_user('user1', 'user1@example.com') == True
    assert user_manager.add_user('user2', 'user2@example.com') == True
    
    # Test original get functionality
    assert user_manager.get_user('user1') == {'email': 'user1@example.com'}
    assert user_manager.get_user('user2') == {'email': 'user2@example.com'}
    
    # Test new update functionality
    assert user_manager.update_user('user1', 'new1@example.com') == True
    assert user_manager.update_user('user2', 'new2@example.com') == True
    
    # Verify updates didn't break original functionality
    assert user_manager.get_user('user1') == {'email': 'new1@example.com'}
    assert user_manager.get_user('user2') == {'email': 'new2@example.com'}
    
    # Verify original add still works
    assert user_manager.add_user('user3', 'user3@example.com') == True

if __name__ == "__main__":
    pytest.main([__file__]) 