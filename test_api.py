# test_api.py

from fastapi.testclient import TestClient
from main import app
import pytest


# (Yeh line ek FastAPI TestClient instance create karta hai, 
# jise aap apne FastAPI app ke endpoints ko test karne ke liye use kar sakte hain.)
client = TestClient(app)


# Test case for creating a new Todo
def test_create_todo():
    # Send a POST request to create a new Todo
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the created Todo's title matches the expected value
    assert response.json()["title"] == "Test Todo"


# Test case for updating an existing Todo
def test_update_todo():
    # Send a PUT request to update an existing Todo (Todo ID: 1)
    response = client.put("/todos/1", json={"title": "Updated Todo", "description": "Updated Description"})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the updated Todo's title matches the expected value
    assert response.json()["title"] == "Updated Todo"


# Test case for deleting an existing Todo
def test_delete_todo():
    # Send a DELETE request to delete an existing Todo (Todo ID: 1)
    response = client.delete("/todos/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the deletion message matches the expected value
    assert response.json()["message"] == "Todo deleted"