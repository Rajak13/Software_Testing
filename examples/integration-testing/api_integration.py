"""
Example demonstrating API integration testing.
This example shows:
1. How to test API endpoints
2. How to handle authentication
3. How to manage test data
"""

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import Dict, List

# Sample application
app = FastAPI()

# In-memory database for testing
class Database:
    def __init__(self):
        self.users: Dict[int, Dict] = {}
        self.next_id = 1
    
    def create_user(self, user_data: Dict) -> int:
        user_id = self.next_id
        self.users[user_id] = {**user_data, 'id': user_id}
        self.next_id += 1
        return user_id
    
    def get_user(self, user_id: int) -> Dict:
        return self.users.get(user_id)
    
    def update_user(self, user_id: int, user_data: Dict) -> bool:
        if user_id not in self.users:
            return False
        self.users[user_id].update(user_data)
        return True
    
    def delete_user(self, user_id: int) -> bool:
        if user_id not in self.users:
            return False
        del self.users[user_id]
        return True

# API endpoints
@app.post("/users/")
def create_user(user_data: Dict):
    db = Database()
    user_id = db.create_user(user_data)
    return {"id": user_id, **user_data}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = Database()
    user = db.get_user(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: Dict):
    db = Database()
    if not db.update_user(user_id, user_data):
        return {"error": "User not found"}, 404
    return {"id": user_id, **user_data}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = Database()
    if not db.delete_user(user_id):
        return {"error": "User not found"}, 404
    return {"message": "User deleted"}

# Test client
client = TestClient(app)

# Test data
test_user = {
    "name": "Test User",
    "email": "test@example.com",
    "age": 30
}

# Integration tests
def test_create_user():
    """Test user creation"""
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_user["name"]
    assert data["email"] == test_user["email"]
    assert data["age"] == test_user["age"]
    assert "id" in data
    return data["id"]

def test_get_user():
    """Test user retrieval"""
    # First create a user
    user_id = test_create_user()
    
    # Then retrieve it
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_user["name"]
    assert data["email"] == test_user["email"]
    assert data["age"] == test_user["age"]

def test_update_user():
    """Test user update"""
    # First create a user
    user_id = test_create_user()
    
    # Update the user
    update_data = {
        "name": "Updated User",
        "email": "updated@example.com",
        "age": 35
    }
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["email"] == update_data["email"]
    assert data["age"] == update_data["age"]

def test_delete_user():
    """Test user deletion"""
    # First create a user
    user_id = test_create_user()
    
    # Delete the user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"
    
    # Verify user is deleted
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404

def test_error_handling():
    """Test error scenarios"""
    # Test getting non-existent user
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"
    
    # Test updating non-existent user
    response = client.put("/users/999", json=test_user)
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"
    
    # Test deleting non-existent user
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"

if __name__ == "__main__":
    pytest.main([__file__]) 