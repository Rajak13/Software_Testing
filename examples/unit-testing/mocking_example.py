"""
Example demonstrating unit testing with mocking.
This example shows:
1. How to use pytest-mock for mocking
2. How to test code with external dependencies
3. How to verify mock calls
"""

import pytest
from datetime import datetime

class Database:
    def get_user(self, user_id: int) -> dict:
        """Simulate database call"""
        raise NotImplementedError("This should be mocked in tests")

class UserService:
    def __init__(self, db: Database):
        self.db = db
    
    def get_user_age(self, user_id: int) -> int:
        """Get user's age from database"""
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        return user['age']

def test_get_user_age_success(mocker):
    """Test successful user age retrieval"""
    # Create mock database
    mock_db = mocker.Mock(spec=Database)
    mock_db.get_user.return_value = {'age': 25}
    
    # Create service with mock database
    service = UserService(mock_db)
    
    # Test the service
    age = service.get_user_age(1)
    
    # Verify results
    assert age == 25
    mock_db.get_user.assert_called_once_with(1)

def test_get_user_age_not_found(mocker):
    """Test user not found scenario"""
    # Create mock database
    mock_db = mocker.Mock(spec=Database)
    mock_db.get_user.return_value = None
    
    # Create service with mock database
    service = UserService(mock_db)
    
    # Test the service
    with pytest.raises(ValueError, match="User not found"):
        service.get_user_age(1)
    
    # Verify mock was called
    mock_db.get_user.assert_called_once_with(1)

class EmailService:
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Simulate email sending"""
        raise NotImplementedError("This should be mocked in tests")

class NotificationService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
    
    def notify_user(self, user_email: str, message: str) -> bool:
        """Send notification to user"""
        return self.email_service.send_email(
            to=user_email,
            subject="Notification",
            body=message
        )

def test_notification_service(mocker):
    """Test notification service with mocked email"""
    # Create mock email service
    mock_email = mocker.Mock(spec=EmailService)
    mock_email.send_email.return_value = True
    
    # Create notification service
    service = NotificationService(mock_email)
    
    # Test sending notification
    result = service.notify_user(
        "user@example.com",
        "Test message"
    )
    
    # Verify results
    assert result == True
    mock_email.send_email.assert_called_once_with(
        to="user@example.com",
        subject="Notification",
        body="Test message"
    )

def test_notification_service_failure(mocker):
    """Test notification service failure"""
    # Create mock email service that fails
    mock_email = mocker.Mock(spec=EmailService)
    mock_email.send_email.return_value = False
    
    # Create notification service
    service = NotificationService(mock_email)
    
    # Test sending notification
    result = service.notify_user(
        "user@example.com",
        "Test message"
    )
    
    # Verify results
    assert result == False
    mock_email.send_email.assert_called_once_with(
        to="user@example.com",
        subject="Notification",
        body="Test message"
    )

if __name__ == "__main__":
    pytest.main([__file__]) 